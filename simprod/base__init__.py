#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, getpass

modulepath = None
os.environ["SIMPRODPATH"] = modulepath

simoutput = None
if simoutput is None:
    simoutput = os.getenv("HOME") + "/SimulationJobs"
os.system("mkdir -p " + simoutput)
os.environ["SIMOUTPUT"] = simoutput

# _log_simoutput_ = None
# _if log_simoutput is None :
# _	user = getpass.getuser()
# _	log_simoutput = "/afs/cern.ch/work/{0}/{1}".format( user[0], user )
# _os.system("mkdir -p "+log_simoutput)
# _os.environ["LOG_SIMOUTPUT"] = log_simoutput

from .simjob import *
