#!/usr/bin/python

import os, getpass

modulepath = '/afs/cern.ch/user/m/mmarinan/SimProd'
os.environ["SIMPRODPATH"] = modulepath

simoutput = '/eos/lhcb/user/m/mmarinan/SimulationJobs'
if simoutput is None :
    simoutput = os.getenv("HOME")+"/SimulationJobs"
os.system("mkdir -p "+simoutput)
os.environ["SIMOUTPUT"] = simoutput

log_simoutput = '/afs/cern.ch/work/m/mmarinan/SimulationJobs'
if log_simoutput is None :
	user = getpass.getuser()
	log_simoutput = "/afs/cern.ch/work/{0}/{1}".format( user[0], user )
os.system("mkdir -p "+log_simoutput)
os.environ["LOG_SIMOUTPUT"] = log_simoutput

from .simjob import *

