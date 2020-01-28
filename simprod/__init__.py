#!/usr/bin/python

import os, getpass

modulepath = '/share/lphe/home/marinang/SimulationProduction'
os.environ["SIMPRODPATH"] = modulepath

simoutput = '/panfs/marinang/SimulationJobs'
if simoutput is None :
    simoutput = os.getenv("HOME")+"/SimulationJobs"
os.system("mkdir -p "+simoutput)
os.environ["SIMOUTPUT"] = simoutput

#_log_simoutput_ = None
#_if log_simoutput is None :
#_	user = getpass.getuser()
#_	log_simoutput = "/afs/cern.ch/work/{0}/{1}".format( user[0], user )
#_os.system("mkdir -p "+log_simoutput)
#_os.environ["LOG_SIMOUTPUT"] = log_simoutput

from .simjob import *

