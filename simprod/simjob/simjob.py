#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Matthieu Marinangeli
# Mail: matthieu.marinangeli@cern.ch
# Description: simulation job class

import os
import time
from random import randint, shuffle
import warnings
import glob
from tqdm import tqdm
from colorama import Fore
import sys
import numpy as np

from .setup import DoProd, checksiminputs
from .utils import *
from .utils.utilities import (
    green,
    red,
    blue,
    cyan,
    magenta,
    cdefault,
    baserunnumber,
    silentrm,
)
from .utils.Database import getdatabase
from .utils.Status import resolve_status
from .utils.GetEvtType import getevttype
from .utils.MoveJobs import Move, EosMove
from .exceptions import NotPreparedError, SubmittedError, PreparedError
from .type_checkers import (
    check_int,
    check_year,
    check_simcond,
    check_simmodel,
    check_stripping,
    check_polarities,
    check_flag,
    check_str,
    check_infiles,
)

from tinydb import Query

DATABASE, STORAGE = getdatabase()

py3 = (
    sys.version_info[0] > 2
)  # creates boolean value for test that Python major version > 2


class JobCollection(object):
    """
    Container class of the SimulationJob.
    """

    def __init__(self):

        self.jobs = {}
        n_jobs = len(self.collection)

        if IsHTCondor():
            from utils.HTCondorUtils import Scheduler

            self._job_kwargs = {"scheduler": Scheduler()}
        else:
            self._job_kwargs = {"scheduler": None}

        if n_jobs > 0:

            print(red("\nLoading Jobs:"))
            t = tqdm(total=n_jobs)

            for k in self.keys:

                job_k = self.collection.get(doc_id=k)

                if job_k["status"] == "completed":
                    self.jobs[k] = None
                else:
                    self.jobs[k] = SimulationJob.from_doc(job_k, **self._job_kwargs)

                t.update(1)

            t.close()

        self.update()

    @property
    def collection(self):
        """
        Returns the table 'jobs' in the databse.
        """
        return DATABASE.table("jobs")

    @property
    def keys(self):
        """
        Returns keys of SimulationJob in the collection.
        """
        return sorted([j.doc_id for j in self.collection.all()], key=int)

    def __str__(self):
        """
        Returns the str representation of the JobCollection, which is a str with
        one line per SimulationJob in the collection with the following description:
            * number/key.
            * status.
            * evttype.
            * year.
            * number of events.
            * number of SimulationSubJob's.
            * number of running SimulationSubJob's.
            * number of completed SimulationSubJob's.
            * number of failed SimulationSubJob's.
        """

        self.update()

        toprint = []
        toprint.append("{0} jobs".format(len(self.jobs)))

        h_job = "    #job "
        h_status = "       status "
        h_evttype = "       evttype "
        h_year = "   year "
        h_nevents = "  #events "
        h_subjobs = "  #subjobs "
        h_running = "  #R "
        h_completed = "  #C "
        h_failed = "  #F "

        tojoin = [
            h_job,
            h_status,
            h_evttype,
            h_year,
            h_nevents,
            h_subjobs,
            h_running,
            h_completed,
            h_failed,
        ]
        header = "|".join(tojoin) + "|"
        line = "".join(["-" for i in range(len(header) - 2)])

        toprint.append(line)
        toprint.append(header)
        toprint.append(line)

        for k in self.keys:
            job = self.jobs[k]

            if job is not None:
                status = job.status
                evttype = job.evttype
                year = job.year
                nevents = job.nevents
                subjobs = job.nsubjobs
                if status in ["new", "prepared", "corrupted"]:
                    nrunning = 0
                    ncompleted = 0
                    nfailed = 0
                else:
                    nrunning = len(job.select("running", False))
                    ncompleted = len(job.select("completed", False))
                    nfailed = len(job.select("failed", False))
            else:
                job_doc = self.collection.get(doc_id=k)
                status = job_doc["status"]
                evttype = job_doc["evttype"]
                year = job_doc["year"]
                nevents = job_doc["nevents"]
                subjobs = job_doc["nsubjobs"]
                nrunning = job_doc["nrunning"]
                ncompleted = job_doc["ncompleted"]
                nfailed = job_doc["nfailed"]

            if status == "submitted":
                color = cyan
            elif status == "submitting":
                color = magenta
            elif status == "running":
                color = green
            elif status == "completed":
                color = blue
            elif status == "failed":
                color = red
            else:
                color = cdefault

            p_job = "{n:{fill}{al}{w}} ".format(
                w=(len(h_job) - 1), al=">", fill="", n=k
            )

            p_status = "{n:{fill}{al}{w}} ".format(
                w=(len(h_status) - 1), al=">", fill="", n=status
            )

            p_evttype = "{n:{fill}{al}{w}} ".format(
                w=(len(h_evttype) - 1), al=">", fill="", n=evttype
            )

            p_year = "{n:{fill}{al}{w}} ".format(
                w=(len(h_year) - 1), al=">", fill="", n=year
            )

            p_nevents = "{n:{fill}{al}{w}} ".format(
                w=(len(h_nevents) - 1), al=">", fill="", n=nevents
            )

            p_subjobs = "{n:{fill}{al}{w}} ".format(
                w=(len(h_subjobs) - 1), al=">", fill="", n=subjobs
            )

            p_running = "{n:{fill}{al}{w}} ".format(
                w=(len(h_running) - 1), al=">", fill="", n=nrunning
            )

            p_completed = "{n:{fill}{al}{w}} ".format(
                w=(len(h_completed) - 1), al=">", fill="", n=ncompleted
            )

            p_failed = "{n:{fill}{al}{w}} ".format(
                w=(len(h_failed) - 1), al=">", fill="", n=nfailed
            )

            tojoin = [
                p_job,
                p_status,
                p_evttype,
                p_year,
                p_nevents,
                p_subjobs,
                p_running,
                p_completed,
                p_failed,
            ]

            linejob = "|".join(tojoin) + "|"

            toprint.append(color(linejob))

        toprint = "\n".join(toprint)

        return toprint

    def _repr_pretty_(self, p, cycle):
        """
        Method called in IPython to print the representation of the JobCollection.
        """
        if cycle:
            p.text(self.__repr__())
            return
        p.text(self.__str__())

    def __geti__(self, i, printlevel=1):
        """
        Methods to access the i-th SimulationJob in the collection. If the SimulationJob with key i is
        in the collection but not loaded it will be loaded. If the key is larger than the maximum key in the
        in the collection, the database gets updated to fetch newly created SimulationJob's in the simprod
        prompt.

        Args:
            * i (int): key of the SimulationJob to access
            * printlevel (int, default=1): if 1 the loading the of the SimulationJob is printed, if 0 nothing
                is printed

        Returns:
            SimulationJob

        Raises:
            * KeyError if a SimulationJob with key = i is not in the collection.
        """

        if i not in self.keys and i > max(self.keys):
            self.update()
        if i not in self.keys:
            raise KeyError("job {0} not found!".format(i))
        else:
            if self.jobs[i] is None:
                if printlevel > 0:
                    print(green("Loading Job {0}:".format(i)))
                job_i_doc = self.collection.get(doc_id=i)
                job_i = SimulationJob.from_doc(job_i_doc, **self._job_kwargs)
                self.jobs[i] = job_i

            status = self.jobs[i].status

            new_to_prepared = status == "new" and len(self.jobs[i].jobtable) > 0
            prepared_to_new = (
                status in ["prepared", "corrupted"] and len(self.jobs[i].jobtable) == 0
            )

            if new_to_prepared or prepared_to_new:
                job_i_doc = self.collection.get(doc_id=i)
                self.jobs[i] = SimulationJob.from_doc(job_i_doc, **self._job_kwargs)

        return self.jobs[i]

    def __getitem__(self, i):
        """
        Methods to access the i-th SimulationJob in the collection.

        Args:
            * i (int): key of the SimulationJob to access

        Returns:
            SimulationJob

        Raises:
            * KeyError if a SimulationJob with key = i is not in the collection.
        """
        return self.__geti__(i, printlevel=1)

    def __iter__(self):
        """
        Iterates over the SimulationJob's in the collection.
        """
        for k in self.keys:
            yield self.__geti__(k, printlevel=-1)

    def __len__(self):
        """
        Returns the number of SimulationJob in the collection.
        """
        return len(self.collection)

    def select(self, status):
        """
        Selects all the SimulationJob's with the status given as arguments.

        Args:
            * status (str): the status of interest.

        Returns:
            List[SimulationJob]
        """
        return [j for j in self.__iter__() if j.status == status]

    def update(self):
        """
        Method to update the table 'jobs' in the database.
        """

        for job_doc in self.collection.all():
            key = job_doc.doc_id

            if key not in self.jobs:
                for ntry in range(2):
                    self.jobs[key] = SimulationJob.from_doc(job_doc, **self._job_kwargs)
                    if self.jobs[key].status != "failed":
                        break
                    time.sleep(1)
                continue

            job = self.jobs[key]

            if job is None:
                continue

            status = job.status

            if not job.subjobs or len(job.jobtable) == 0:
                self.jobs[key] = SimulationJob.from_doc(job_doc, **self._job_kwargs)
                continue

            elif status in [
                "new",
                "prepared",
                "corrupted",
            ]:
                if status != job_doc["status"]:
                    self.jobs[key] = SimulationJob.from_doc(job_doc, **self._job_kwargs)
                    self.collection.update(dict(status=status), doc_ids=[key])
                else:
                    job._update_job_in_database(update_subjobs_in_database=True)
                continue

            if job_doc["status"] == "submitting" or status == "submitting":
                job._update_job_in_database(update_subjobs_in_database=True)

            if status != job_doc["status"]:
                self.collection.update(dict(status=status), doc_ids=[key])

            if status in ["completed", "failed"]:
                self.jobs[key] = None

        if len(self.jobs) > len(self.keys):
            for k in self.jobs.keys():
                if k not in self.keys:
                    del self.jobs[k]


class SimulationJob(object):
    """
    Class for simulation jobs. It is a container of SimulationSubJob's.

    Args:
        * nevents (int): number of events to simulate.
        * year (int): data taking year to simulate.
        * evttype (int): evttype to generate.
        * neventsjob (int, defautl=50): number of events in each SimulationSubJob
        * polarities (str, default=None): polarities ,'MagUp' or 'MagDown', of the LHCb magnet to simulate.
            By default half of the subjobs have 'MagUp' and the other half have 'MagDown'.
        * simcond (str, default='Sim09h'): version of the simulation conditions.
        * stripping (str/int, default=None): version of the stripping selection, by default it is the latest full
            stripping version (without "r" standing for incremental restripping).
        * turbo (bool, default=False): flag to indicate if the Turbo should be run.
        * mdst (bool, default=False): flag to indicate if the output should a 'mdst' instead of a 'dst'.
        * runnumber (int, optionnal): seed used to generated the events, by default it is computed from the date.
        * decfiles (str, default="v30r46"): version of the DecFiles package.
        * redecay (bool, default=False): flag to indicate wether the signal in the simulated events should be
            redecayed for faster simulation.
        * simmodel (str, default="pythia8"): indicates the event generator. By the default it is 'pythia8' but
        'BcVegPy' is available.
        * keeplogs (bool, default=False): flag to indicate if the output and error logs of the jobs should be
            kept even in the job has been completed successfully.
        * keepxmls: (bool, default=False): flag to indicate if the xml file produced by Gauss should be kept.
    """

    def __init__(
        self,
        nevents,
        year,
        evttype,
        neventsjob=50,
        polarities=None,
        simcond="Sim09h",
        stripping=None,
        turbo=False,
        mudst=False,
        runnumber=baserunnumber(),
        decfiles="v30r46",
        redecay=False,
        simmodel="pythia8",
        keeplogs=True,
        keepxmls=True,
        **kwargs
    ):
        self.subjobs = {}
        self._options = {}

        non_supported_kws = [{"supported": "polarities", "non_supported": ["polarity"]}]
        for nkws in non_supported_kws:
            for ns in nkws["non_supported"]:
                if ns in kwargs:
                    msg = "The keyword {kw_ns} is not supported, use {kw_s} instead."
                    msg = msg.format(kw_ns=ns, kw_s=nkws["supported"])
                    warnings.warn(blue(msg))

        self._status = "new"
        self._nevents = check_int(nevents, "nevents")
        self._year = check_year(year)
        self._decfiles = check_str(decfiles, "decfiles")
        self.evttype = check_int(evttype, "evttype")
        self._neventsjob = check_int(neventsjob, "neventsjob")
        self._polarities = check_polarities(polarities)
        self._simcond = check_simcond(simcond)
        self._stripping = check_stripping(stripping)
        self._turbo = check_flag(turbo, "turbo")
        self._mudst = check_flag(mudst, "mudst")
        self._runnumber = check_int(runnumber, "runnumber")
        self._redecay = check_flag(redecay, "redecay")
        self._simmodel = check_simmodel(simmodel)
        self._keeplogs = check_flag(keeplogs, "keeplogs")
        self._keepxmls = check_flag(keepxmls, "keepxmls")
        self._inscreen = kwargs.get("inscreen", False)

        _basedir = os.getenv("SIMOUTPUT")
        if not _basedir:
            _basedir = os.getenv("HOME") + "/SimulationJobs"

        self._options["basedir"] = kwargs.get("basedir", _basedir)

        self.htcondor = False

        if IsSlurm():
            self._options["loginprod"] = True

        elif IsHTCondor() or IsLSF():
            if os.getenv("LOG_SIMOUTPUT"):
                self._options["loginprod"] = kwargs.get("loginprod", False)
            else:
                self._options["loginprod"] = kwargs.get("loginprod", True)

            if not self._options["loginprod"]:
                self._options["logdir"] = kwargs.get(
                    "logdir", os.getenv("LOG_SIMOUTPUT")
                )

        self.scheduler = kwargs.get("scheduler", None)

        if IsHTCondor():
            self.htcondor = True
            if self.scheduler is None:
                self.scheduler = Scheduler()

        self.deliveryclerk = DeliveryClerk(
            inscreen=self._inscreen, scheduler=self.scheduler
        )

        if not self.options.get("loginprod", True):
            self._options["logdestdir"] = "{0}/{1}".format(
                self.options["logdir"], self.subdir
            )

        self.screensessions = []

        self.database = DATABASE

        self.jobnumber = None

        if kwargs.get("newjob", True):
            jobstable = self.database.table("jobs")
            jobstable.insert(self.dump())
            self.jobnumber = jobstable._last_id
        else:
            self.jobnumber = kwargs.get("jobnumber", None)

    @property
    def jobtable(self):
        """
        Returns the table of the SimulationJob in the database.
        """
        return self.database.table("job_{}".format(self.jobnumber))

    @property
    def range_subjobs(self):
        """
        Returns a generator of the keys of the SimulationSubJob's.
        """
        for n in range(self.nsubjobs):
            yield n + 1

    @property
    def is_prepared(self):
        status = self.status

        if status == "new":
            return False
        else:
            return True

    @property
    def is_submitted(self):
        status = self.status

        if status in ["new", "prepared", "corrupted"]:
            return False
        else:
            return True

    @property
    def nevents(self):
        """
        Returns the number of events simulated.
        """
        return self._nevents

    @nevents.setter
    def nevents(self, nevents):
        """
        Sets the number of events simulated.

        Args:
            * nevents (int/flaot): if it is float it will be converted to an int.

        Raises:
            * TypeError is nevents is not a float/int.
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """

        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._nevents = check_int(nevents, "nevents")

    @property
    def neventsjob(self):
        """
        Returns the number of events for each subjob.
        """
        return self._neventsjob

    @neventsjob.setter
    def neventsjob(self, nevents):
        """
        Sets the number of events for each subjob.

        Args:
            * nevents (int/flaot): if it is float it will be converted to an int.

        Raises:
            * TypeError is nevents is not a float/int.
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._neventsjob = check_int(nevents, "neventsjob")

    @property
    def nsubjobs(self):
        """
        Returns the number SimulationSubJob's.
        """
        self._nsubjobs = int(self.nevents / self.neventsjob)
        return self._nsubjobs

    @property
    def evttype(self):
        """
        Returns the evttype simulated.
        """
        return self._evttype

    @evttype.setter
    def evttype(self, evttype):
        """
        Sets the evttype simulated.
        """

        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)

        self._evttype = check_int(evttype, "evttype")
        optfile = "{0}/EvtTypes/{1}/{1}.py".format(os.getenv("SIMPRODPATH"), evttype)

        if not os.path.isfile(optfile):
            getevttype(evttype=evttype, decfiles=self.decfiles)

        self._optfile = optfile

    @property
    def optfile(self):
        """
        Returns the options file where the evttype is defined.
        """
        return self._optfile

    @property
    def simcond(self):
        """
        Returns the version of the simulation condittions.
        """
        return self._simcond

    @simcond.setter
    def simcond(self, version):
        """
        Sets the version of the simulation conditions.

        Args:
            * version (str): version of the simulation conditions.

        Raises:
            * ValueError if version is not in [Sim09b, Sim09c, Sim09e, Sim09f, Sim09h].
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._simcond = check_simcond(version)

    @property
    def simmodel(self):
        """
        Returns the event generator.
        """
        return self._simmodel

    @simmodel.setter
    def simmodel(self, model):
        """
        Sets the event generator.

        Args:
            * model (str): name of the event generator.

        Raises:
            * ValueError if model is not in [pythia8, BcVegPy].
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._simmodel = check_simmodel(model)

    @property
    def doprod(self):
        """
        Returns the bash script that is send to the batch system to run the simulation.abs
        """
        return DoProd(self.simcond, self.year)

    @property
    def stripping(self):
        """
        Returns stripping version.
        """
        return self._stripping

    @stripping.setter
    def stripping(self, version):
        """
        Sets the stripping version.

        Args:
            * version (str): the stripping version.

        Raises:
            * ValueError if model is not in [21, 24, 28, 24r1, 24r1p1, 28r1, 28r1p1, 28r2,
                29r2, 29r2p1, 34, 34r0p1].
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._stripping = check_stripping(version)

    @property
    def year(self):
        """
        Returns the data taking year to simulate.
        """
        return self._year

    @year.setter
    def year(self, year):
        """
        Sets the data taking year to simulate.

        Args:
            * year (int): year to simulate.

        Raises:
            * TypeError if year is not an int.
            * ValueError if year is not in [2011, 2012, 2015, 2016, 2017, 2018].
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._year = check_year(year)

    @property
    def polarities(self):
        """
        Returns the polarities of the LHCb magnet to simulate. If None is returned it means that half
        of the subjobs have MagUp and the other subjobs have MagDown.
        """
        return self._polarities

    @polarities.setter
    def polarities(self, polarity):
        """
        Sets the polarities of the LHCb magnet to simulate.

        Args:
            * polarity (str): the polarity.

        Raises:
            * TypeError if polarity is not a str.
            * ValueError if polarity is not in [MagUp, MagDown].
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._polarities = check_polarities(polarity)

    @property
    def keys(self):
        """
        Returns the keys of the SimulationSubJob's.
        """
        return self.subjobs.keys()

    @property
    def options(self):
        """
        Returns a dictionnary of options that is shared to the SimulationSubJob's.
        """
        return self._options

    @property
    def subdir(self):
        """
        Returns the sub-directory where the output of the subjobs will be produced.
        """
        subdir = "simProd_{0}_{1}".format(self.evttype, self.simcond)
        if self.turbo:
            subdir += "_Turbo"
        if self.mudst:
            subdir += "_muDST"
        if self.redecay:
            subdir += "_ReDecay"

        self.options["subdir"] = subdir

        return subdir

    @property
    def proddir(self):
        """
        Returns the directory where the output of the subjobs will be produced.
        """
        self._proddir = "{0}/{1}".format(self.options["basedir"], self.subdir)
        return self._proddir

    @property
    def destdir(self):
        """
        Returns the directory where the output of the subjobs will be stored.
        """
        self._destdir = "{0}/{1}/{2}/{3}".format(
            self.options["basedir"], self.evttype, self.year, self.simcond
        )
        if self._redecay:
            self._destdir += "_ReDecay"
        return self._destdir

    @property
    def turbo(self):
        """
        Indicates if the Turbo step will be run or not.
        """
        return self._turbo

    @turbo.setter
    def turbo(self, boolean):
        """
        Sets if the Turbo step will be run or not.

        Args:
            * boolean (bool): if True Turbo is run, if False it is not.

        Raises:
            * TypeError if boolean is not a bool.
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._turbo = check_flag(boolean, "turbo")

    @property
    def mudst(self):
        """
        Indicates if the output of the subjobs will be `dst` or `mdst` files.
        """
        return self._mudst

    @mudst.setter
    def mudst(self, boolean):
        """
        Sets the output format of the subjobs to `mdst` if True or `dst` if False.

        Args:
            * boolean (bool): if True `mdst` output is used, if False `dst` is used.

        Raises:
            * TypeError if boolean is not a bool.
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._mudst = check_flag(boolean, "mudst")

    @property
    def decfiles(self):
        """
        Returns the version of the DecFiles package.
        """
        return self._decfiles

    @decfiles.setter
    def decfiles(self, version):
        """
        Sets the version of the DecFiles package.

        Args:
            * version (str): version of the DecFiles package.

        Raises:
            * TypeError if version is not a str.
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._decfiles = check_str(version, "decfiles")

    @property
    def redecay(self):
        """
        Indicates if the simulated signal should be redecayed.
        """
        return self._redecay

    @redecay.setter
    def redecay(self, boolean):
        """
        Sets if the simulated signal should be redecayed.

        Args:
            * boolean (bool): if True ReDecay used, if False ReDecay it is not used.

        Raises:
            * TypeError if boolean is not a bool.
            * PreparedError if the job is prepared.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)
        elif self.is_prepared:
            msg = "This property cannot be modified once the job is prepared."
            msg = " Call the method cancelpreparation to unprepare to the job."
            raise PreparedError(msg)

        self._redecay = check_flag(boolean, "redecay")

    @property
    def keeplogs(self):
        """
        Indicates if the output and error log files should be kept even if the subjobs have been
        completed successfully.
        """
        return self._keeplogs

    @keeplogs.setter
    def keeplogs(self, boolean):
        """
        Sets if the output and error log files should be kept even if the subjobs have been
        completed successfully.

        Args:
            * boolean (bool): if True logs are kept, if False they are not.

        Raises:
            * TypeError if boolean is not a bool.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)

        self._keeplogs = check_flag(boolean, "keeplogs")

    @property
    def keepxmls(self):
        """
        Indicates the generator level informations stored in xml files should be kept.
        """
        return self._keepxmls

    @keepxmls.setter
    def keepxmls(self, boolean):
        """
        Sets if the generator level informations stored in xml files should be kept.

        Args:
            * boolean (bool): if True xml files are kept, if False they are not.

        Raises:
            * TypeError if boolean is not a bool.
            * SubmittedError if the job is submitted.
        """
        if self.is_submitted:
            msg = "This property cannot be modified once the job is submitted."
            raise SubmittedError(msg)

        self._keepxmls = check_flag(boolean, "keepxmls")

    def getrunnumber(self, sjn=0):
        """
        Returns the runnumber for a given subjob:
            self._runnumber + sjn

        Args:
            sjn (int, default=0)

        Raise:
            TypeError is sjn is not a int

        Returns:
            int
        """
        if not isinstance(sjn, int):
            raise TypeError(
                "{0} has a non valid {1} type for sjn, must be a int!".format(
                    sjn, type(sjn)
                )
            )

        if sjn is None:
            return self._runnumber
        else:
            return self._runnumber + sjn

    def prepare(self, update_table=True, infiles=None):
        """
        Prepare the job. Calls the method _preparesubjobs that creates the SimulationSubJob's.

        Args:
            update_table (bool, default=True): if True update the table 'jobs' in the database.
            infiles (List[str], optionnal): list of files to needed for the subjobs.
        """
        if len(self.subjobs) < 1:

            checksiminputs(self)

            if self.nsubjobs == 0:

                self.neventsjob = int(self.nevents / 2)
                self.nevents = self.neventsjob * 2

            def sample_polarities():
                polarities = ["MagUp", "MagDown"]
                i = randint(0, 1)
                p1 = polarities.pop(i)
                p2 = polarities[0]

                polarity = [p1 for i in range(1, int(self.nsubjobs / 2) + 1)]
                polarity += [
                    p2 for i in range(int(self.nsubjobs / 2) + 1, self.nsubjobs + 1)
                ]
                return shuffle(polarity)

            if not isinstance(self._polarities, list):
                if self._polarities is None:
                    self._polarities = sample_polarities()
                elif self._polarities in ["MagUp", "MagDown"]:
                    self._polarities = [self._polarities for i in self.range_subjobs]
                else:
                    raise ValueError(
                        "Invalid value '{}' for polarities. Valid choices are ['MagUp', 'MagDown']".format(
                            self._polarities
                        )
                    )
            else:
                if len(self._polarities) != self.nsubjobs:
                    self._polarities = sample_polarities()
                elif not all(p in ["MagUp", "MagDown"] for p in self._polarities):
                    raise ValueError("Invalid values for polarities.")

        for n in self.range_subjobs:
            if self.subjobs.get(n, None) is not None:
                continue

            self._preparesubjobs(n, infiles=infiles)

        # update status
        self.status

        if update_table:
            self._update_job_in_database(update_subjobs_in_database=True)

    def _preparesubjobs(self, sjn, infiles=None):
        """
        Prepares the SimulationJob with subjob number sjn.

        Args:
            sjn (int): the subjob number
            infiles (List[str], optionnal): list of files to needed for the subjobs.
        """

        if self._polarities:
            polarity = self._polarities[sjn - 1]
        else:
            if sjn <= int(self.nsubjobs / 2):
                polarity = "MagUp"
            else:
                polarity = "MagDown"

        if sjn not in self.keys:
            runnumber = self.getrunnumber(sjn)
            self.subjobs[sjn] = SimulationSubJob(
                parent=self,
                polarity=polarity,
                runnumber=runnumber,
                subjobnumber=sjn,
                infiles=infiles,
            )

    def send(self):
        """
        Send the subjobs to the batch system.

        Raises:
            * NotPreparedError if the job is not prepared.
        """

        if not self.is_prepared:
            raise NotPreparedError("Please 'prepare' the job before sending it!")

        if self.last_status == "completed":
            print("Job is completed. There is nothing to send.")
        else:
            failedsubjobs = self.select("failed")
            for sj in failedsubjobs:
                sj.reset()

            self.status
            self.deliveryclerk.send_job(self, STORAGE)
            self._update_job_in_database(update_subjobs_in_database=True)
            STORAGE.flush()

    def cancelpreparation(self):
        """
        Unprepares the SimulationJob.
        """

        if not self.is_prepared:
            raise NotPreparedError(
                "The job needs to be prepared before being unprepared."
            )

        if self.is_submitted:
            raise SubmittedError("Cannot unprepare once the job is submitted.")

        self.subjobs = {}
        self.jobtable.purge()
        self._status = "new"

    def remove(self):
        """
        Removes the SimulationJob from the database.
        """
        if self.jobnumber:
            info_msg = "INFO\tremoving job {0}".format(self.jobnumber)
        else:
            info_msg = "INFO\tremoving job"
        print(info_msg)

        if self.status in ["running", "submitting"]:
            sjkill = self.deliveryclerk.kill(job=self)

        if len(self.keys) > 0:

            for n in self.range_subjobs:
                sj = self[n]

                if sj and sj.status == "running":
                    sj.kill(storeparent=False, sjkill=sjkill)

        self.database.purge_table("job_{}".format(self.jobnumber))
        self.database.table("jobs").remove(doc_ids=[self.jobnumber])

    def __getitem__(self, sjn):
        """
        Methods to access the sjn-th SimulationSubJob.

        Args:
            * sjn (int): subjob number

        Returns:
            SimulationSubJob

        Raises:
            * KeyError if a SimulationSubJob with key = i is not in the collection.
        """
        if len(self.keys) == 0:
            msg = "Cannot access the subjobs is the job is unprepared. Please call the method 'prepare'."
            raise NotPreparedError(msg)

        if sjn not in self.keys:
            if sjn < min(self.keys) or sjn > min(self.keys):
                raise KeyError("SimulationSub {0} not found!".format(sjn))
            else:
                self.subjobs[sjn] = self._load_subjob(sjn, force_load=True)

        subjob = self.subjobs[sjn]

        if subjob is None:
            self.subjobs[sjn] = self._load_subjob(sjn, force_load=True)

        return self.subjobs[sjn]

    def __setitem__(self, sjn, subjob):
        """
        Sets the sjn-th SimulationSubJob.

        Args:
            * sjn (int): subjob number
            * subjob (SimulationSubJob): the subjob

        Raises:
            * TypeError if sjn is not int or subjob is not a SimulationSubJob.
        """

        if not isinstance(sjn, int):
            raise TypeError(
                "{0} has a non valid {1} type for sjn, must be a int!".format(
                    sjn, type(sjn)
                )
            )

        if not isinstance(subjob, SimulationSubJob):
            raise TypeError(
                "{0} has a non valid {1} type for sjn, must be a SimulationSubJob!".format(
                    subjob, type(subjob)
                )
            )

        self.subjobs[sjn] = subjob

    def __iter__(self):
        """
        Iterates over the SimulationSubJob's.
        """
        for n in self.range_subjobs:
            yield self[n]

    def select(self, status, update=True):
        """
        Selects all the SimulationSubJob's with the status given as arguments.

        Args:
            * status (str): the status of interest.
            * update (bool, default=True): if True updated status are taken into account, otherwise the
                previous status are.

        Returns:
            List[SimulationSubJob]

        Raises:
            * NotPreparedError if the job is not prepared.
        """

        if self.last_status in ["new", "corrupted"]:
            raise NotPreparedError("Cannot use this method if the job is not prepared!")
        try:
            if update:
                return [self[n] for n in self.range_subjobs if self[n].status == status]
            else:
                return [
                    self[n] for n in self.range_subjobs if self[n].last_status == status
                ]
        except AttributeError:
            return []

    @property
    def last_status(self):
        """
        Returns the non updated status of the SimulationJob.
        """
        return self._status

    @property
    def status(self):
        """
        Returns the updated status of the SimulationJob.
        """

        if len(self.keys) == 0:
            return "new"

        if not self.last_status == "completed":

            table_from_clerk = self.deliveryclerk.get_update_subjobs_in_database(self)

            status_list = []

            for n in self.range_subjobs:

                sj_doc = self.jobtable.get(doc_id=n)
                sj = self.subjobs[n]

                if table_from_clerk is not None:
                    sj_doc_from_clerk = table_from_clerk.get(Query().subjobnumber == n)
                else:
                    sj_doc_from_clerk = None

                if sj is None:
                    if sj_doc is None:
                        status = "notfound"
                    else:
                        status = sj_doc["status"]
                else:
                    status = sj.status
                    jobid = sj.jobid

                    if sj_doc_from_clerk is not None:
                        assert sj_doc_from_clerk["runnumber"] == self.getrunnumber(n)
                        states = ["error", "notfound", "failed"]

                        if (
                            sj_doc_from_clerk["jobid"] != status
                            and status == "new"
                            and self.deliveryclerk.getstatus(sj_doc_from_clerk["jobid"])
                            not in states
                        ):

                            jobid = sj_doc_from_clerk["jobid"]
                            sj.jobid = jobid
                            sj._status = resolve_status(
                                status, sj_doc_from_clerk["status"], sj.output
                            )
                            status = sj_doc_from_clerk["status"]

                    if sj_doc["jobid"] != jobid or sj_doc["status"] != status:
                        sj_doc["jobid"] = jobid
                        sj_doc["status"] = status

                        self.jobtable.update(sj_doc, doc_ids=[n])

                #                    if status in ["completed", "failed"]:
                #                        self.subjobs[n] = None

                status_list.append(status)

            status_counts, counts = np.unique(status_list, return_counts=True)
            sc = dict(zip(status_counts, counts))

            if sc.get("notfound", 0) > 0:
                status = "corrupted"
            else:
                if sc.get("new", 0) == self.nsubjobs:
                    status = "prepared"
                elif (
                    sc.get("submitted", 0) > 0 or sc.get("running", 0) > 0
                ) and sc.get("new", 0) > 0:
                    status = "submitting"
                elif sc.get("running", 0) > 0:
                    status = "running"
                elif sc.get("completed", 0) == self.nsubjobs:
                    status = "completed"
                    self.deliveryclerk.clear(self)
                else:
                    if sc.get("completed", 0) + sc.get("failed", 0) == self.nsubjobs:
                        status = "failed"
                    else:
                        status = "submitted"

            if status != self.last_status:
                info_msg = "INFO\tstatus of job {0} changed from '{1}' to '{2}'"
                info_msg = info_msg.format(self.jobnumber, self.last_status, status)

                print(info_msg)
                self._update_job_in_database(True)

            self._status = status

        return self._status

    def dump(self):
        """
        Serialize the SimulationJob to a dictionnary.

        Returns:
            dictionnary
        """

        status = self.last_status

        outdict = {
            "evttype": self.evttype,
            "year": self.year,
            "nevents": self.nevents,
            "neventsjob": self.neventsjob,
            "nsubjobs": self.nsubjobs,
            "runnumber": self._runnumber,
            "simcond": self.simcond,
            "polarities": self.polarities,
            "stripping": self.stripping,
            "simmodel": self.simmodel,
            "mudst": self.mudst,
            "turbo": self.turbo,
            "basedir": self.options["basedir"],
            "proddir": self.proddir,
            "destdir": self.destdir,
            "subdir": self.options["subdir"],
            "loginprod": self.options["loginprod"],
            "screensessions": self.screensessions,
            "status": status,
            "keeplogs": self.keeplogs,
            "keepxmls": self.keepxmls,
            "redecay": self.redecay,
            "deliveryclerk": self.deliveryclerk.outdict(),
        }

        outdict["nrunning"] = 0
        outdict["ncompleted"] = 0
        outdict["nfailed"] = 0

        if outdict["status"] not in ["new", "prepared"]:
            try:
                outdict["nrunning"] = len(self.select("running", False))
                outdict["ncompleted"] = len(self.select("completed", False))
                outdict["nfailed"] = len(self.select("failed", False))
            except TypeError:
                pass

        if not self.options["loginprod"]:
            outdict["logdir"] = self.options["logdir"]
            outdict["logdestdir"] = self.options["logdestdir"]

        return outdict

    def _update_job_in_database(self, update_subjobs_in_database=False):
        """
        Method to update the SimulationJob and the 'jobs' table in the database.

        Args:
            update_subjobs_in_database (bool, default=False): Flag to indicate wheter or not to update the
                subjobs in the database.
        """

        jobstable = self.database.table("jobs")

        jobstable.update(self.dump(), doc_ids=[self.jobnumber])

        if update_subjobs_in_database:
            for n in self.range_subjobs:

                job = self[n]
                status = job._status

                if job is None:
                    continue

                if status == "new" and isinstance(job.jobid, int):
                    job._status = resolve_status(status, "submitted", job.output)
                    continue

                if status != "submitted":
                    continue

                if status == "completed":
                    continue
                else:
                    job._update_subjob_in_database()

    @classmethod
    def from_dict(cls, dict, jobnumber, inscreen=False, printlevel=1, **kwargs):
        """
        Construct the SimulationJob from a dictionnary.

        Args:
            * dict (dictionnary)
            * jobnumber (int)
            * inscreen (bool, default=False): indicates wether or not this method is called in a screen
                session.
            * printlevel (int, default=1): if 1 the loading the of the SimulationJob is printed, if 0 nothing
                is printed.

        Returns:
            SimulationJob
        """

        if not py3:
            for k in dict.keys():
                if isinstance(dict[k], unicode):
                    dict[k] = dict[k].encode("utf-8")

        simjob = cls(
            evttype=dict["evttype"],
            year=dict["year"],
            nevents=dict["nevents"],
            neventsjob=dict["neventsjob"],
            runnumber=dict["runnumber"],
            polarities=dict.get("polarities", None),
            simcond=dict["simcond"],
            stripping=dict["stripping"],
            simmodel=dict.get("simmodel", "pythia8"),
            mudst=dict["mudst"],
            turbo=dict["turbo"],
            basedir=dict["basedir"],
            newjob=False,
            jobnumber=jobnumber,
            **kwargs
        )

        simjob.jobnumber = jobnumber
        simjob._options["subdir"] = dict["subdir"]
        simjob._options["loginprod"] = dict["loginprod"]
        simjob.screensessions = dict["screensessions"]
        simjob._status = dict.get("status", "new")
        simjob._keeplogs = dict.get("keeplogs", True)
        simjob._keepxmls = dict.get("keepxmls", True)
        simjob._redecay = dict.get("redecay", False)

        if not simjob._options["loginprod"]:
            simjob._options["logdir"] = dict["logdir"]
            simjob._options["logdestdir"] = dict["logdestdir"]

        simjob._options["cpumemory"] = dict.get("cpumemory", None)
        if not simjob._options["cpumemory"]:
            simjob._options["cpumemory"] = dict.get("cpu", None)

        simjob.deliveryclerk = DeliveryClerk.from_dict(dict["deliveryclerk"], **kwargs)

        if len(simjob.jobtable) > 0:

            if printlevel > 0:
                t = tqdm(
                    total=simjob.nsubjobs,
                    bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET),
                    desc=cyan("\tLoading subjobs"),
                )
            else:
                t = None

            simjob.subjobs = {
                n: simjob._load_subjob(n, t, printlevel, False)
                for n in simjob.range_subjobs
            }

            if printlevel > 0:
                t.close()

        return simjob

    @classmethod
    def from_doc(cls, doc, inscreen=False, printlevel=1, **kwargs):
        """
        Construct the SimulationJob from a TinyDB document.

        Args:
            * doc (tinydb.Document)
            * inscreen (bool, default=False): indicates wether or not this method is called in a screen
                session.
            * printlevel (int, default=1): if 1 the loading the of the SimulationJob is printed, if 0 nothing
                is printed.

        Returns:
            SimulationJob
        """

        jobnumber = doc.doc_id
        simjob = cls.from_dict(doc, jobnumber, inscreen, printlevel, **kwargs)

        return simjob

    def _load_subjob(self, sjn, pbar=None, printlevel=0, force_load=False):
        """
        Load SimulationSubJob's from the SimulationJob table. By default completed or failed subjobs are
        not loaded unless force_load is True.

        Args:
            * sjn (int): subjob number.
            * pbar (optional): progress bar.
            * printlevel (int, default=1): if 1 the loading the of the SimulationJob is printed, if 0 nothing
                is printed.
            * force_load (bool, default=False): if True the subjob is loaded even if it is completed or
                has failed.

        Returns:
            SimulationSubJob

        Raises:
            * TypeError if doc is not a tinydb.table.Document.
        """

        sj_doc = self.jobtable.get(doc_id=sjn)

        if sj_doc is not None:
            status = sj_doc["status"]

            if status in ["completed", "failed"] and not force_load:
                sj = None
            else:
                sj = SimulationSubJob.from_doc(self, sj_doc)
        else:
            sj = None

        if printlevel > 0:
            pbar.update(1)

        return sj

    def __str__(self):
        """
        Returns the str representation of the SimulationJob, which is a str with
        one line per SimulationSubJob with the following description:
            * number/key.
            * job ID.
            * status.
            * runnumber.
            * polarity.
            * number of events.

        Returns:
            str
        """

        if len(self.subjobs) > 0 and len(self.jobtable) > 0:

            toprint = []

            toprint.append(
                "evttype: {0}; year: {1}; #events {2}; stripping {3}; simcond {4}; {5} jobs".format(
                    self.evttype,
                    self.year,
                    self.nevents,
                    self.stripping,
                    self.simcond,
                    self.nsubjobs,
                )
            )

            h_job = "    #job "
            h_jobID = "    job ID "
            h_status = "       status "
            h_runnumber = "      runnumber "
            h_polarity = "   polarity "
            h_nevents = "  #events "

            header = [h_job, h_jobID, h_status, h_runnumber, h_polarity, h_nevents]
            header = "|".join(header) + "|"
            line = "".join(["-" for i in range(len(header) - 2)])

            toprint.append(line)
            toprint.append(header)
            toprint.append(line)

            for n in self.range_subjobs:

                sj_doc = self.jobtable.get(doc_id=n)

                if self.subjobs[n] is None:
                    status = sj_doc["status"]
                    jobID = sj_doc["jobid"]
                    runnumber = self.getrunnumber(n)
                    polarity = sj_doc["polarity"]
                else:
                    job = self[n]
                    status = job.status
                    jobID = job.jobid
                    runnumber = job.runnumber
                    polarity = job.polarity

                    _dict = {}

                    if sj_doc["jobid"] != job.jobid:
                        _dict["jobid"] = job.jobid
                    if sj_doc["status"] != job.status:
                        _dict["status"] = job.status

                    if len(_dict) > 0:
                        self.jobtable.update(_dict, doc_ids=[n])

                nevents = self.neventsjob

                if status == "submitted":
                    color = cyan
                elif status == "new":
                    color = cdefault
                elif status == "running":
                    color = green
                elif status == "completed":
                    color = blue
                elif status == "failed":
                    color = red

                p_job = "{n:{fill}{al}{w}} ".format(
                    w=(len(h_job) - 1), al=">", fill="", n=n
                )

                p_jobID = "{n:{fill}{al}{w}} ".format(
                    w=(len(h_jobID) - 1), al=">", fill="", n=jobID
                )

                p_status = "{n:{fill}{al}{w}} ".format(
                    w=(len(h_status) - 1), al=">", fill="", n=status
                )

                p_runnumber = "{n:{fill}{al}{w}} ".format(
                    w=(len(h_runnumber) - 1), al=">", fill="", n=runnumber
                )

                p_polarity = "{n:{fill}{al}{w}} ".format(
                    w=(len(h_polarity) - 1), al=">", fill="", n=polarity
                )

                p_nevents = "{n:{fill}{al}{w}} ".format(
                    w=(len(h_nevents) - 1), al=">", fill="", n=nevents
                )

                linejob = (
                    "|".join(
                        [p_job, p_jobID, p_status, p_runnumber, p_polarity, p_nevents]
                    )
                    + "|"
                )

                toprint.append(color(linejob))

            toprint = "\n".join(toprint)

        else:
            toprint = self.__repr__()

        return toprint

    def _repr_pretty_(self, p, cycle):
        """
        Method called in IPython to print the representation of the SimulationJob.
        """
        if cycle:
            p.text(self.__repr__())
            return
        p.text(self.__str__())


class SimulationSubJob(object):
    """
    Simulation subjob.
    """

    def __init__(
        self, parent, polarity, runnumber, subjobnumber, infiles=None, **kwargs
    ):
        self.parent = parent
        self.polarity = polarity
        self.runnumber = runnumber
        self.subjobnumber = subjobnumber
        self._jobid = None
        self.send_options = self.parent.options.copy()
        self._infiles = check_infiles(infiles)
        self.send_options["infiles"] = self._infiles

        self.jobname = "{0}_{1}_{2}evts_s{3}_{4}".format(
            self.parent.year,
            self.polarity,
            self.parent.neventsjob,
            self.parent.stripping,
            self.runnumber,
        )

        self.send_options["jobname"] = self.jobname

        self.jobdir = "{0}/{1}".format(self.parent.proddir, self.jobname)

        ext = "dst"
        if self.parent.mudst:
            ext = "mdst"

        self.prodfile = "{0}/{1}_events.{2}".format(
            self.jobdir, self.parent.neventsjob, ext
        )

        self.destfile = "{0}/{1}/{2}evts_s{3}_{4}.{5}".format(
            self.parent.destdir,
            self.polarity,
            self.parent.neventsjob,
            self.parent.stripping,
            self.runnumber,
            ext,
        )

        if not self.send_options["loginprod"]:
            self.logjobdir = "{0}/{1}".format(
                self.send_options["logdestdir"], self.jobname
            )

        self._status = "new"

        if kwargs.get("newsubjob", True):
            self.parenttable.insert(self.dump())
            assert self.parenttable._last_id == subjobnumber

        if kwargs.get("to_store", False):
            self._update_subjob_in_database()

    @property
    def jobid(self):
        return self._jobid

    @jobid.setter
    def jobid(self, jobid):
        if self.last_status in ["submitted", "running"]:
            raise SubmittedError(
                "Cannot change the jobid of the subjob once submitted."
            )
        self._jobid = jobid

    @property
    def keeplog(self):
        return self.parent.keeplogs

    @property
    def keepxml(self):
        return self.parent.keepxmls

    @property
    def parenttable(self):
        return self.parent.jobtable

    @property
    def infiles(self):
        return self._infiles

    @infiles.setter
    def infiles(self, files):

        files = check_infiles(files)

        self._infiles = files
        self.send_options["infiles"] = files
        self._update_subjob_in_database()

    def send(self):

        if self.last_status in ["new", "failed"]:
            if self.last_status == "failed":
                self.reset()

            self.jobid = self.parent.deliveryclerk.send_subjob(self)

            if self.jobid:
                self._status = "submitted"
                print(
                    blue(
                        "{0}/{1} jobs submitted!".format(
                            int(self.subjobnumber), self.parent.nsubjobs
                        )
                    )
                )
            else:
                print(
                    red(
                        "job {0}/{1} submission failed, try later!".format(
                            int(self.subjobnumber), self.parent.nsubjobs
                        )
                    )
                )

            self._update_subjob_in_database()

    @property
    def last_status(self):
        return self._status

    @property
    def status(self):

        if self.jobid is not None:

            previous_status = self.last_status

            if previous_status not in ["failed", "completed"]:
                status = self.parent.deliveryclerk.getstatus(self.jobid)
                self._status = resolve_status(previous_status, status, self.output)

            if previous_status != self._status:

                info_msg = "INFO\tstatus of subjob {0}.{1} changed from '{2}' to '{3}'"
                info_msg = info_msg.format(
                    self.parent.jobnumber,
                    self.subjobnumber,
                    previous_status,
                    self._status,
                )

                print(info_msg)
                self._update_subjob_in_database()

            if self._status == "completed":
                if not self.output == self.destfile and not self.output == "":
                    self._move_jobs()
            elif self._status == "failed":
                self._empty_proddir(keep_log=True)

        else:
            if self._status != "new":
                print("PROBLEM")
                print(self._status)
                print(self.parent.jobnumber, self.subjobnumber)
                self._status = "new"

        return repr(self._status)

    @property
    def output(self):
        if os.path.isfile(self.prodfile):
            return self.prodfile
        elif os.path.isfile(self.destfile):
            return self.destfile
        else:
            return ""

    def reset(self):

        if self.last_status == "running":
            self.kill()

        self._empty_proddir()
        self.jobid = None
        self._status = "new"
        self._update_subjob_in_database()

    def command(self):
        command = dict(doprod=self.parent.doprod)
        command["args"] = []
        command["args"].append(self.parent.optfile)
        command["args"].append(self.parent.neventsjob)
        command["args"].append(self.polarity)
        command["args"].append(self.runnumber)
        command["args"].append(self.parent.turbo)
        command["args"].append(self.parent.mudst)
        command["args"].append(self.parent.stripping)
        command["args"].append(self.parent.redecay)
        command["args"].append(self.parent.simmodel)
        return command

    def kill(self, storeparent=True, sjkill=True):

        info_msg = "INFO\tkilling subjob {0}.{1}"
        info_msg = info_msg.format(self.parent.jobnumber, self.subjobnumber)
        print(info_msg)

        if sjkill:
            if self._status != "new":
                self.parent.deliveryclerk.killsubjob(self.jobid)

        self._status = "failed"
        self._update_subjob_in_database()
        if storeparent:
            self.parent._update_job_in_database()
        self._empty_proddir()

    def _empty_proddir(self, keep_log=False):
        if os.path.isdir(self.jobdir):
            if keep_log and self.send_options["loginprod"]:
                files = glob.iglob(self.jobdir + "/*")
                for f in files:
                    if "out" in f:
                        continue
                    elif "err" in f:
                        continue
                    else:
                        os.remove(f)
            else:
                silentrm(self.jobdir)

        if not self.send_options["loginprod"] and not keep_log:
            if os.path.isdir(self.logjobdir):
                silentrm(self.logjobdir)

    def _move_jobs(self):

        if not os.path.isdir(self.jobdir):
            msg = (
                " WARNING: production folder has been removed, if the jobs is marked as"
            )
            msg += "failed the output hasbeen probably lost!"
            warnings.warn(red(msg), stacklevel=2)

        else:
            dst_prodfile = self.prodfile

            if "eos" in dst_prodfile:
                mover = EosMove
            else:
                mover = Move

            xml_prodfile = os.path.dirname(dst_prodfile) + "/GeneratorLog.xml"
            dst_destfile = self.destfile
            xml_destfile = os.path.dirname(self.destfile) + "/xml/{0}.xml".format(
                self.runnumber
            )

            info_msg = "INFO\tMoving output of subjob {0}.{1} to {2}!"
            info_msg = info_msg.format(
                self.parent.jobnumber, self.subjobnumber, dst_destfile
            )
            print(info_msg)

            if os.path.isfile(dst_prodfile):
                mover(dst_prodfile, dst_destfile)
            else:
                warn_msg = red(
                    "WARNING\tdst output is not found. It has probably been moved or erased manually"
                )
                print(warn_msg)

            if self.keepxml:

                info_msg = (
                    "INFO\tMoving generator informations of subjob {0}.{1} to {2}!"
                )
                info_msg = info_msg.format(
                    self.parent.jobnumber, self.subjobnumber, xml_destfile
                )
                print(info_msg)

                if os.path.isfile(xml_prodfile):
                    mover(xml_prodfile, xml_destfile)
                else:
                    warn_msg = red(
                        "WARNING\tGeneratorLog.xml is not found. It has probably been moved or erased manually"
                    )
                    print(warn_msg)

            self._empty_proddir(self.keeplog)

    def dump(self):

        outdict = {
            "runnumber": self.runnumber,
            "polarity": self.polarity,
            "jobid": self.jobid,
            "status": repr(self._status),
            "infiles": self.infiles,
        }

        if not self.send_options["loginprod"]:
            outdict["logjobdir"] = self.logjobdir

        return outdict

    def _update_subjob_in_database(self):
        self.parenttable.update(self.dump(), Query().runnumber == self.runnumber)

    @classmethod
    def from_dict(cls, parent, dict, subjobnumber, to_store=False):

        simsubjob = cls(
            parent=parent,
            polarity=dict["polarity"],
            runnumber=dict["runnumber"],
            subjobnumber=subjobnumber,
            newsubjob=False,
            infiles=dict.get("infiles", None),
        )

        simsubjob.jobid = dict["jobid"]
        simsubjob.send_options["infiles"] = dict.get("infiles", None)

        status = dict["status"]

        simsubjob._status = status

        if not simsubjob.send_options["loginprod"]:
            simsubjob.logjobdir = dict["logjobdir"]

        if to_store:
            simsubjob._update_subjob_in_database()

        return simsubjob

    @classmethod
    def from_doc(cls, parent, doc, to_store=False):

        subjobnumber = doc.doc_id
        simsubjob = cls.from_dict(parent, doc, subjobnumber, to_store)

        return simsubjob
