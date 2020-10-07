#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Matthieu Marinangeli
# Mail: matthieu.marinangeli@cern.ch

from subprocess import Popen, PIPE
from datetime import datetime
from random import randint
import os
import getpass
import time
import sys

from tinydb import TinyDB, JSONStorage
from tinydb.middlewares import CachingMiddleware

from .utilities import red, blue
from .submit import main as submit
from .ScreenUtils import SendInScreen, KillScreenSession

DEBUG = 0

try:
    import pyslurm

    haspyslurm = True
except ImportError:
    haspyslurm = False

py3 = (
    sys.version_info[0] > 2
)  # creates boolean value for test that Python major version > 2

if py3:
    from importlib import reload
else:
    from imp import reload


def Kill(ID):

    kill = Popen(["scancel", str(ID)], stdout=PIPE, stderr=PIPE)
    _, _ = kill.communicate()


def GetStatus(ID):

    if haspyslurm:
        try:
            j = pyslurm.job()
            j = j.find_id(str(ID))[0]
            status = j["job_state"].lower()
        except ValueError:
            status = "notfound"

    else:

        command = ["squeue", "--job", str(ID), "-o", "'%T"]

        if sys.version_info[0] > 2:
            process = Popen(command, stdout=PIPE, stderr=PIPE, encoding="utf8")
        else:
            process = Popen(command, stdout=PIPE, stderr=PIPE)

        out, err = process.communicate()

        if "slurm_load_jobs error: Invalid job id specified" in err:
            status = "notfound"
        else:
            try:
                status = out.split("\n")[1].replace("'", "").lower()

                if status == "pending":
                    status = "submitted"
                elif status in ["runnning", "completing"]:
                    status = "running"
                elif status == "completed":
                    status = "completed"
                elif status in ["suspended", "cancelled", "stopped"]:
                    status = "cancelled"
                elif status in ["failed", "timeout"]:
                    status = "failed"
            except IndexError:
                status = "submitted"

    if status == "pending":
        status = "submitted"
    if status == "cancelled":
        status = "failed"

    return status


def GetConfig():
    if DEBUG > 1:
        print("In GetConfig")

    def_config = DefaultSlurmConfig()

    if "lphe" in os.getenv("HOSTNAME"):

        if DEBUG > 1:
            print("LPHE")

        configfile = "/share/lphe/home/marinang/SimulationLPHEConfig.py"
        configdir = "/share/lphe/home/marinang/"
        if os.path.isfile(configfile):

            if "SimulationLPHEConfig" in sys.modules:
                import SimulationLPHEConfig

                reload(SimulationLPHEConfig)
            else:
                try:
                    import SimulationLPHEConfig
                except ImportError:
                    sys.path.insert(0, configdir)
                    import SimulationLPHEConfig
            config = SimulationLPHEConfig.config()
        else:
            config = def_config
    else:
        config = def_config

    if DEBUG > 1:
        print("New config:")
        print(config)
        print("Out of GetConfig\n")

    return config


def DefaultSlurmConfig():

    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()

    config = {}

    # During the day less job submission

    if hour > 5 and hour < 22:
        nsimjobs = 400
        nsimuserjobs = 100
        nuserjobs = 150
        npendingjobs = 40
        nfreenodes = 4
    else:
        nsimjobs = 800
        nsimuserjobs = 200
        nuserjobs = 300
        npendingjobs = 60
        nfreenodes = 1

    if weekday == 5 or weekday == 6:
        nsimjobs *= 1.5
        nsimuserjobs *= 1.5
        nuserjobs *= 1.5
        npendingjobs *= 1.5

    config["nsimjobs"] = nsimjobs
    config["nsimuserjobs"] = nsimuserjobs
    config["nuserjobs"] = nuserjobs
    config["npendingjobs"] = npendingjobs
    config["nfreenodes"] = nfreenodes
    config["nodestoexclude"] = []
    config["cpumemory"] = 2800
    config["totmemory"] = 4140
    config["time"] = 20

    return config


def DefaultSlurmOptions():

    config = GetConfig()
    return config


def SubCondition(Options):

    user = getpass.getuser()

    if DEBUG > 0:
        print("In SubCondition")
        print(Options)

    # additionnal submission conditions for SLURM batch system

    ti, tf = Options["subtime"][0], Options["subtime"][1]
    if ti < tf:
        allowed_time = range(ti, tf + 1)
    elif tf < ti:
        allowed_time = range(ti, 24) + range(0, tf + 1)

    Nsimjobs_user = int(
        os.popen("echo $(squeue -u {0} | grep -c 'simProd')".format(user)).read()
    )
    Nsimjobs_total = int(os.popen("echo $(squeue | grep -c 'simProd')").read())
    Njobs_user = int(os.popen("echo $(squeue  | grep -c '{0}')".format(user)).read())
    Npendjobs_user = int(
        os.popen("echo $(squeue -u {0} | grep -c 'PD')".format(user)).read()
    )

    now = datetime.now()
    hour = now.hour

    # conditions
    time = hour in allowed_time
    simjobs_total = Options["nsimjobs"] <= Nsimjobs_total
    simjobs_user = Options["nsimuserjobs"] <= Nsimjobs_user
    jobs_user = Options["nuserjobs"] <= Njobs_user
    pendjobs_user = Options["npendingjobs"] <= Npendjobs_user

    if not time:
        print(red("Jobs are sent between {0}h and {1}h!".format(ti, tf)))
        Submission = False
    elif simjobs_user:
        print(
            red(
                "You have already submitted {0} simulation jobs. Wait for submission!".format(
                    Nsimjobs_user
                )
            )
        )
        Submission = False
    elif simjobs_total:
        print(
            red(
                "{0} simulation jobs are submitted. Wait for submission!".format(
                    Nsimjobs_total
                )
            )
        )
        Submission = False
    elif jobs_user:
        print(
            red(
                "You have already submitted {0} jobs. Wait for submission!".format(
                    Njobs_user
                )
            )
        )
        Submission = False
    elif pendjobs_user:
        print(
            red(
                "You have already {0} jobs pending. Wait for submission!".format(
                    Npendjobs_user
                )
            )
        )
        Submission = False
    elif (
        time
        and not simjobs_user
        and not simjobs_total
        and not jobs_user
        and not pendjobs_user
    ):
        Submission = True

    if DEBUG > 0:
        print("Out of SubCondition\n")

    return Submission


class DeliveryClerk(object):
    def __init__(self, **kwargs):

        if DEBUG > 1:
            print("In DeliveryClerk.__init__:")

        self.defaults = []
        options = {}

        options["subtime"] = kwargs.get("subtime", [0, 23])

        parameters = [
            "nsimjobs",
            "nuserjobs",
            "npendingjobs",
            "nfreenodes",
            "nodestoexclude",
            "cpumemory",
            "totmemory",
            "nsimuserjobs",
            "time",
        ]

        for p in parameters:
            options[p] = kwargs.get(p, self.default_options[p])
            if DEBUG > 1:
                print(p, options[p], self.default_options[p])
            if kwargs.get(p, None) is None:
                self.defaults.append(p)

        if DEBUG > 1:
            print("defaults", self.defaults)

        self.screensessions = []

        self._options = options

        self.inscreen = kwargs.get("inscreen", False)

        for var in self.options.keys():
            self.addvar(var)

        if DEBUG > 1:
            print("Out of DeliveryClerk.__init__: \n")

    @property
    def options(self):
        if DEBUG > 0:
            print("In DeliveryClerk.options update")
            print(self._options)
        for opt in self.defaults:
            self._options[opt] = self.default_options[opt]
        if DEBUG > 0:
            print(self._options)
            print("Out DeliveryClerk.options update\n")
        return self._options

    @options.setter
    def options(self, dict):
        self._options = dict

    @property
    def default_options(self):
        return DefaultSlurmOptions()

    def outdict(self):
        return {
            "options": self.options,
            "screensessions": self.screensessions,
            "defaults": self.defaults,
        }

    @classmethod
    def from_dict(cls, dict, **kwargs):
        deliveryclerk = cls(**dict["options"])
        deliveryclerk.screensessions = dict["screensessions"]
        deliveryclerk.defaults = dict["defaults"]

        return deliveryclerk

    def new_send_options(self, options):
        options = dict(options)
        options["time"] = self.options["time"]
        options["cpumemory"] = self.options["cpumemory"]
        options["totmemory"] = self.options["totmemory"]
        options["nfreenodes"] = self.options["nfreenodes"]
        options["nodestoexclude"] = self.options["nodestoexclude"]
        options["slurm"] = True
        return options

    def send_job(self, job, storage, *args, **kwargs):

        if self.inscreen:
            for n in job.range_subjobs:
                job[n].send()
        else:

            storage.flush()

            cmdpy = screencommandfile(job)

            screename = cmdpy.replace(".py", "")
            screename = screename.replace(os.path.dirname(screename) + "/", "")

            _id = SendInScreen(screename, cmdpy)

            print(red("Job submission is done in a screen session!"))

            self.screensessions.append({"name": screename, "id": _id})

    def send_subjob(self, subjob):

        SUBMIT = False
        while SUBMIT is False:
            SUBMIT = SubCondition(self.options)
            if not SUBMIT:
                time.sleep(randint(0, 20) * 60)

        if subjob._status == "new" or subjob._status == "failed":
            if subjob._status == "failed":
                subjob.reset()

            send_options = subjob.send_options
            command = subjob.command()["doprod"] + " "
            command += " ".join(str(a) for a in subjob.command()["args"])
            send_options["command"] = command
            send_options["slurm"] = True
            send_options = self.new_send_options(send_options)
            subjobid = submit(**send_options)

            return subjobid

    def send_subjob_inscreen(self, subjob, storage):

        subjobid = None

        SUBMIT = False
        while SUBMIT is False:
            SUBMIT = SubCondition(self.options)
            if not SUBMIT:
                storage.flush()
                time.sleep(randint(0, 10) * 60)

        if subjob._status == "new" or subjob._status == "failed":
            if subjob._status == "failed":
                subjob.reset()

            send_options = subjob.send_options
            command = subjob.command()["doprod"] + " "
            command += " ".join(str(a) for a in subjob.command()["args"])
            send_options["command"] = command
            send_options["slurm"] = True
            send_options = self.new_send_options(send_options)
            subjobid = submit(**send_options)

            subjob.jobid = subjobid

            if subjob.jobid:
                subjob._status = "submitted"

                time.sleep(0.07)
                print(
                    blue(
                        "{0}/{1} jobs submitted!".format(
                            subjob.subjobnumber, subjob.parent.nsubjobs
                        )
                    )
                )
                time.sleep(0.07)
            else:
                print(
                    red(
                        "job {0}/{1} submission failed, try later!".format(
                            subjob.subjobnumber, subjob.parent.nsubjobs
                        )
                    )
                )

            subjob._update_subjob_in_database()

    def get_update_subjobs_in_database(self, job):

        simprod = os.getenv("SIMPRODPATH")
        name = "job_{0}".format(job.jobnumber)
        fname = simprod + "/" + name + ".json"

        if os.path.isfile(fname):
            DATABASE = getdatabase(fname)
            table = DATABASE.table(name)
            #DATABASE.close()
            return table, DATABASE
        else:
            return None

    def getstatus(self, ID):
        return GetStatus(ID)

    def clear(self, job):

        simprod = os.getenv("SIMPRODPATH")
        name = "{0}/job_{1}".format(simprod, job.jobnumber)
        dbname = name + ".json"
        pyname = name + ".py"

        if os.path.isfile(dbname):
            os.remove(dbname)
        if os.path.isfile(pyname):
            os.remove(pyname)

    def kill(self, **kwargs):
        for sc in self.screensessions:
            KillScreenSession(sc["name"])
            self.screensessions = []
        return True

    def killsubjob(self, ID):
        Kill(ID)

    def addvar(self, var):
        def make_get_set(var):
            def getter(self):
                return self.options[var]

            def setter(self, value):
                if not isinstance(value, type(self.default_options[var])):
                    msg = "A {} is required!".format(type(self.default_options[var]))
                    raise TypeError(msg)

                self.options[var] = value
                if var in self.defaults:
                    self.defaults.remove(var)

            return getter, setter

        get_set = make_get_set(var)

        setattr(DeliveryClerk, var, property(*get_set))
        self.__dict__[var] = getattr(DeliveryClerk, var)


def getdatabase(file):
    storage = CachingMiddleware(JSONStorage)
    storage.WRITE_CACHE_SIZE = 20
    return TinyDB(file, storage=storage)


def screencommandfile(job):

    simprod = os.getenv("SIMPRODPATH")

    name = "{0}/job_{1}".format(simprod, job.jobnumber)
    pyfile = name + ".py"
    dbasefile = name + ".json"
    if job.status == "new" and os.path.isfile(dbasefile):
        os.remove(dbasefile)

    f = open(pyfile, "w")
    f.write("#!/usr/bin/python\n\n")

    f.write("import os\n")
    f.write("import time\n")
    f.write("from tinydb import TinyDB, JSONStorage, Query\n")
    f.write("from tinydb.middlewares import CachingMiddleware\n")
    f.write("os.environ['SIMPRODPATH'] = '{0}'\n".format(os.getenv("SIMPRODPATH")))
    f.write("os.environ['SIMOUTPUT'] = '{0}'\n".format(os.getenv("SIMOUTPUT")))
    f.write("from simprod import SimulationJob, SimulationSubJob\n\n")

    f.write("time.sleep(1.5)\n\n")

    f.write("storage = CachingMiddleware(JSONStorage)\n")
    f.write("storage.WRITE_CACHE_SIZE = 10\n")
    f.write("jsonfile='{}'\n".format(dbasefile))
    f.write("if os.path.isfile(jsonfile):\n")
    f.write("\tos.remove(jsonfile)\n")
    f.write("DATABASE = TinyDB(jsonfile, storage=storage)\n")

    f.write("job_dict = {}\n".format(job.dump()))

    f.write("job = SimulationJob.from_dict(job_dict, {})\n".format(job.jobnumber))

    f.write("job.database = DATABASE\n\n")

    f.write("query = Query()\n\n")

    if job.status == "new":
        f.write("job.prepare(update_table=False)\n")
        f.write("for n in job.range_subjobs:\n")
        f.write("\tjob_dict = job[n].dump()\n")
        f.write("\tjob_dict['subjobnumber'] = n\n")
        towrite = "\tjob.jobtable.upsert(job_dict, Query().runnumber"
        towrite += " == job.getrunnumber(n))\n"
        f.write(towrite)
        towrite = "\tjob.deliveryclerk.send_subjob_inscreen(job[n], storage)\n"
        f.write(towrite)
    else:
        for sj in job.select("new", update=True):
            sjnum = sj.subjobnumber
            towrite = "job_dict_{0} = {1}\n"
            f.write(towrite.format(sjnum, sj.dump()))
            towrite = "job_dict_{0}['subjobnumber'] = {0}\n"
            f.write(towrite.format(sjnum))
            towrite = "job[{0}] = SimulationSubJob.from_dict(job, job_dict_{0}, {0}, to_store=False)\n"
            f.write(towrite.format(sjnum))
            towrite = "job.jobtable.upsert(job_dict_{0}, query.runnumber"
            towrite += " == job.getrunnumber({0}))\n"
            f.write(towrite.format(sjnum))
            towrite = "job.deliveryclerk.send_subjob_inscreen(job[{}], storage)\n\n"
            f.write(towrite.format(sjnum))

    f.write("\n")
    f.write("os.remove(__file__)\n\n")
    f.write("DATABASE.close()\n")
    f.close()

    return pyfile
