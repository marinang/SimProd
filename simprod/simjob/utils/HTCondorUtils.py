#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Matthieu Marinangeli
# Mail: matthieu.marinangeli@cern.ch

from subprocess import Popen, PIPE
import os
import getpass
import datetime
import shutil
import subprocess as sub

from .dependencies import LazyModule
from .utilities import red, blue
from .submit import SendCommand

htcondor = LazyModule("htcondor")


def DefaultHTCondorOptions():

    options = {}
    options["jobflavour"] = "workday"

    return options


def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line


class Scheduler:
    def __init__(self):
        self._htcondor = htcondor.Schedd()
        self._cached_query = NoneQuery()

    def getquery(self):

        if not self._cached_query.isvalid:
            msg = red("Failed to query job status... Try later!")

            user = getpass.getuser()
            try:
                query = self._htcondor.query(
                    'User=="{0}@cern.ch"'.format(user),
                    ["ClusterID", "JobStatus", "ProcID"],
                )

                if not query:
                    queryresult = NoneQuery()
                else:
                    queryresult = QueryResult(query)

            except (RuntimeError, IOError):
                print(msg)
                queryresult = BadQuery()

            self._cached_query = queryresult

        return self._cached_query

    def act(self, *args, **kwargs):
        self._htcondor.act(*args, **kwargs)

    def renew(self):
        self._htcondor = htcondor.Schedd()


class BadQuery(object):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def isvalid(self):
        return False


class NoneQuery(object):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def isvalid(self):
        return False


class QueryResult(object):
    def __init__(self, query):

        self._result = {}
        for q in query:
            if q["ClusterID"] not in self._result:
                self._result[q["ClusterID"]] = {}
            self._result[q["ClusterID"]][q["ProcID"]] = q["JobStatus"]

        self.creation_time = datetime.datetime.now()

    @property
    def isvalid(self):
        if self._result:
            now = datetime.datetime.now()
            elapsedTime = now - self.creation_time
            minutes = divmod(elapsedTime.total_seconds(), 60)[0]
            if minutes > 3:
                return False
            else:
                return True
        else:
            return False

    def getstatuscode(self, clusterID, procID):
        try:
            return self._result[clusterID][procID]
        except KeyError:
            return None


class DeliveryClerk(object):
    def __init__(self, **kwargs):

        default_options = DefaultHTCondorOptions()
        self.default_options = default_options
        self._schedd = kwargs.get("scheduler")

        self.defaults = []
        options = {}

        options["subtime"] = kwargs.get("subtime", [0, 23])

        options["jobflavour"] = kwargs.get("jobflavour", default_options["jobflavour"])
        self.defaults += ["jobflavour"]

        self.options = options

        self.addvar(
            "jobflavour",
            allowed_values=[
                "espresso",
                "microcentury",
                "longlunch",
                "workday",
                "tomorrow",
                "testmatch",
                "nextweek",
            ],
        )

    @property
    def schedd(self):
        return self._schedd

    def outdict(self):
        return {"options": self.options}

    @classmethod
    def from_dict(cls, dict, **kwargs):
        deliveryclerk = cls(**dict["options"])
        deliveryclerk._schedd = kwargs.get("scheduler", None)
        return deliveryclerk

    def send_job(self, job, *args, **kwargs):

        logdir = job.options["logdestdir"]

        if not os.path.exists(job.proddir):
            os.makedirs(job.proddir)
        if not os.path.exists(job.destdir):
            os.makedirs(job.destdir)
        if not os.path.exists(logdir):
            os.makedirs(logdir)

        subfile = "{logdir}/run.sub".format(logdir=logdir)
        runfile = subfile.replace(".sub", ".sh")

        if os.path.isfile(subfile):
            os.remove(subfile)
        if os.path.isfile(runfile):
            os.remove(runfile)

        doprod = "{0}/{1}".format(logdir, os.path.basename(job.doprod))

        if os.path.isfile(doprod):
            os.remove(doprod)

        shutil.copyfile(job.doprod, doprod)
        sub.call(["chmod", "775", doprod])

        create_runfile(runfile, doprod)

        condor = open(subfile, "w")
        condor.write("executable = {runfile}\n".format(runfile=runfile))
        condor.write("output = $(subjob_log_dir)/out\n")
        condor.write("error = $(subjob_log_dir)/err\n")
        condor.write("log = {logdir}/$(ClusterId).log\n".format(logdir=logdir))
        condor.write(
            '+JobFlavour = "{jobflavour}"\n\n'.format(
                jobflavour=self.options["jobflavour"]
            )
        )

        submitted_jobs = []

        ext = "mdst" if job.mudst else "dst"
        nevts = job.neventsjob

        for n in job.range_subjobs:
            sj = job[n]
            if sj._status == "new":
                sjlogdir = "{logdir}/{sjname}".format(logdir=logdir, sjname=sj.jobname)
                if os.path.isdir(sjlogdir):
                    shutil.rmtree(sjlogdir, ignore_errors=True)
                os.makedirs(sjlogdir)
                if os.path.isdir(sj.jobdir):
                    shutil.rmtree(sj.jobdir, ignore_errors=True)
                os.makedirs(sj.jobdir)

                if sj.infiles:
                    condor.write(
                        "transfer_input_files = {0}\n".format(",".join(sj.infiles))
                    )

                condor.write("subjob_log_dir={sjlogdir}\n".format(sjlogdir=sjlogdir))
                args = " ".join(str(a) for a in sj.command()["args"])
                condor.write("arguments = {args}\n".format(args=args))
                totransfer = 'transfer_output_remaps = "{nevts}_events.{ext}={prodfile} '.format(
                    nevts=nevts, ext=ext, prodfile=sj.prodfile
                )
                totransfer += ' ; GeneratorLog.xml={dir}/GeneratorLog.xml"\n'.format(
                    dir=sj.jobdir
                )
                condor.write(totransfer)
                condor.write("queue\n\n")
                submitted_jobs.append(sj)
        condor.close()

        command = "condor_submit {subfile}".format(subfile=subfile)

        print(blue("Submitting jobs: ...."))

        out = SendCommand(command)
        try:
            ClusterID = int(float(out.split("\n")[1].split(" ")[-1]))
            print(blue(out.split("\n")[1]))
        except IndexError:
            print(red("job {0} submission failed, try later!".format(job.jobnumber)))
            ClusterID = None

        if ClusterID is not None:
            for n, sj in enumerate(submitted_jobs):
                sj.jobid = "{0}.{1}".format(ClusterID, n)
                sj._status = "submitted"

    def send_subjob(self, subjob):
        if subjob._status == "new" or subjob._status == "failed":
            if subjob._status == "failed":
                subjob.reset()

            job = subjob.parent

            logdir = job.options["logdestdir"]

            if not os.path.exists(job.proddir):
                os.makedirs(job.proddir)
            if not os.path.exists(job.destdir):
                os.makedirs(job.destdir)
            if not os.path.exists(logdir):
                os.makedirs(logdir)

            subfile = "{logdir}/run_sj_{sjnum}.sub".format(
                logdir=logdir, sjnum=subjob.subjobnumber
            )
            runfile = subfile.replace(".sub", ".sh")

            if os.path.isfile(subfile):
                os.remove(subfile)
            if os.path.isfile(runfile):
                os.remove(runfile)

            doprod = "{0}/{1}".format(logdir, os.path.basename(job.doprod))

            if os.path.isfile(doprod):
                os.remove(doprod)

            shutil.copyfile(job.doprod, doprod)
            sub.call(["chmod", "775", doprod])

            create_runfile(runfile, doprod)

            condor = open(subfile, "w")
            condor.write("executable = {runfile}\n".format(runfile=runfile))
            condor.write("output = $(subjob_log_dir)/out\n")
            condor.write("error = $(subjob_log_dir)/err\n")
            condor.write("log = {logdir}/$(ClusterId).log\n".format(logdir=logdir))
            condor.write(
                '+JobFlavour = "{jobflavour}"\n\n'.format(
                    jobflavour=self.options["jobflavour"]
                )
            )

            ext = "mdst" if job.mudst else "dst"
            nevts = job.neventsjob

            sjlogdir = "{logdir}/{sjname}".format(logdir=logdir, sjname=subjob.jobname)
            if os.path.isdir(sjlogdir):
                shutil.rmtree(sjlogdir, ignore_errors=True)
            os.makedirs(sjlogdir)
            if os.path.isdir(subjob.jobdir):
                shutil.rmtree(subjob.jobdir, ignore_errors=True)
            os.makedirs(subjob.jobdir)

            if subjob.infiles:
                condor.write(
                    "transfer_input_files = {0}\n".format(",".join(subjob.infiles))
                )

            condor.write("subjob_log_dir={sjlogdir}\n".format(sjlogdir=sjlogdir))
            args = " ".join(str(a) for a in subjob.command()["args"])
            condor.write("arguments = {args}\n".format(args=args))
            totransfer = 'transfer_output_remaps = "{nevts}_events.{ext}={prodfile} '.format(
                nevts=nevts, ext=ext, prodfile=subjob.prodfile
            )
            totransfer += ' ; GeneratorLog.xml={dir}/GeneratorLog.xml"\n'.format(
                dir=subjob.jobdir
            )
            condor.write(totransfer)
            condor.write("queue\n\n")
            condor.close()

            command = "condor_submit {subfile}".format(subfile=subfile)

            print(blue("Submitting jobs ...."))

            out = SendCommand(command)
            try:
                ClusterID = int(float(out.split("\n")[1].split(" ")[-1]))
                print(blue(out.split("\n")[1]))
            except IndexError:
                print(
                    red("job {0} submission failed, try later!".format(job.jobnumber))
                )
                ClusterID = None

            if ClusterID is not None:
                subjob.jobid = "{0}.{1}".format(ClusterID, subjob.subjobnumber)
                subjob._status = "submitted"

    def parseID(self, ID):
        if not isinstance(ID, str):
            ID = str(ID)

        ClusterID = int(ID.split(".")[0])
        ProcID = int(ID.split(".")[1])
        return ClusterID, ProcID

    def getstatus(self, ID):

        ClusterID, ProcID = self.parseID(ID)
        queryresult = self.schedd.getquery()

        if isinstance(queryresult, BadQuery):
            return "error"
        elif isinstance(queryresult, NoneQuery):
            return "notfound"
        else:
            status_code = queryresult.getstatuscode(ClusterID, ProcID)

            if status_code is None:
                return "notfound"
            else:
                if status_code in [0, 3, 5, 7]:
                    return "failed"
                elif status_code in [1]:
                    return "submitted"
                elif status_code in [2, 6]:
                    return "running"
                elif status_code in [4]:
                    return "completed"
                else:
                    return "notfound"

    def get_update_subjobs_in_database(self, job):
        return None

    def clear(self, job):
        pass

    def kill(self, **kwargs):
        job = kwargs["job"]

        cluster_ids = []
        for sj in job:
            ID = sj.jobid
            if ID is None:
                continue
            ClusterID, ProcID = self.parseID(ID)

            if ClusterID not in cluster_ids:
                cluster_ids.append(ClusterID)

        for cid in cluster_ids:
            try:
                self.schedd.act(htcondor.JobAction.Remove, "ClusterId=={0}".format(cid))
            except RuntimeError:
                kill = Popen(["condor_rm", str(cid)], stdout=PIPE, stderr=PIPE)
                out, err = kill.communicate()

        return False

    def killsubjob(self, ID):
        try:
            ClusterID, ProcID = self.parseID(ID)
            self.schedd.act(
                htcondor.JobAction.Remove,
                "ClusterId=={0} && ProcID=={1}".format(ClusterID, ProcID),
            )
        except RuntimeError:
            kill = Popen(["condor_rm", str(ID)], stdout=PIPE, stderr=PIPE)
            out, err = kill.communicate()

    def addvar(self, var, allowed_values=[]):
        def make_get_set(var):
            def getter(self):
                return self.options[var]

            def setter(self, value):
                if not isinstance(value, self.default_options[var]):
                    msg = "A {} is required!".format(type(self.default_options[var]))
                    raise TypeError(msg)

                if len(allowed_values) > 1 and value not in allowed_values:
                    raise ValueError(
                        "Allowed values for {0} are {1}".format(var, allowed_values)
                    )

                self.options[var] = value
                if var in self.defaults:
                    self.defaults.remove(var)

            return getter, setter

        get_set = make_get_set(var)

        setattr(DeliveryClerk, var, property(*get_set))
        self.__dict__[var] = getattr(DeliveryClerk, var)


def create_runfile(namefile, doprod):

    user = getpass.getuser()

    runscript = open(namefile, "w")
    runscript.write("#!/bin/bash\n")
    runscript.write("shopt -s expand_aliases\n")
    runscript.write('export PATH="/bin:/usr/local/bin:/usr/bin:$PATH"\n')
    runscript.write('export HOME="{}"\n'.format(os.environ["HOME"]))
    runscript.write('export USER="{user}"\n'.format(user=user))
    runscript.write("source /cvmfs/lhcb.cern.ch/group_login.sh\n")
    runscript.write("{doprod} $1 $2 $3 $4 $5 $6 $7 $8 $9\n".format(doprod=doprod))
    runscript.close()

    sub.call(["chmod", "775", namefile])
