#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch

from subprocess import Popen, PIPE
from datetime import datetime
import os
import getpass
from .utils import *
import time
import sys
import pyslurm

def KillSlurm( ID ):
	
	kill = Popen(['scancel',str(ID)], stdout=PIPE, stderr=PIPE)
	_, _ = kill.communicate()
			
def GetSlurmStatus( ID ):
		
	try:
		j = pyslurm.job()
		j = j.find_id(str(ID))[0]
		status = j["job_state"].lower()
	except ValueError:
		status = "notfound"
		
	return status
	
def GetConfig():
		
	def_config = DefaultSlurmConfig() 
	
	if "lphe" in os.getenv("HOSTNAME"):
		configfile = "/share/lphe/home/marinang/SimulationLPHEConfig.py"
		configdir  = "/share/lphe/home/marinang/"
		if os.path.isfile(configfile):
			try:
				from SimulationLPHEConfig import config as _conf
			except ImportError:
				sys.path.insert(0, configdir)
				from SimulationLPHEConfig import config	as _conf
			config = _conf()
		else:
			config = def_config		
	else:
		config = def_config
			
	return config
			
def DefaultSlurmConfig( ):
	
	now     = datetime.now()
	hour    = now.hour
	weekday = now.weekday()
	
	config = {}
	
	### During the day less job submission
		
	if hour > 5 and hour < 22:
		nsimjobs     = 400
		nsimuserjobs = 100
		nuserjobs    = 150
		npendingjobs = 40
		nfreenodes   = 4
	else:
		nsimjobs     = 800
		nsimuserjobs = 200
		nuserjobs    = 300
		npendingjobs = 60
		nfreenodes   = 1
		
	if weekday == 5 or weekday == 6:
		nsimjobs     *= 1.5
		nsimuserjobs *= 1.5
		nuserjobs    *= 1.5
		npendingjobs *= 1.5
		
	config["nsimjobs"]     = nsimjobs
	config["nsimuserjobs"] = nsimuserjobs
	config["nuserjobs"]    = nuserjobs
	config["npendingjobs"] = npendingjobs
	config["nfreenodes"]   = nfreenodes
	config["cpu"]          = 4140
			
	return config
	
def DefaultSlurmOptions( ):
	
	config = GetConfig()
	return config
				
def SubCondition( Options ):
	
	user = getpass.getuser()
		
	#additionnal submission conditions for SLURM batch system 
		
	ti, tf = Options['subtime'][0], Options['subtime'][1]
	if ti < tf:
		allowed_time = range(ti,tf+1)
	elif tf < ti:
		allowed_time = range(ti,24) + range(0,tf+1)
			
				
	Nsimjobs_user  = int( os.popen( "echo $(squeue -u {0} | grep -c 'simProd')".format(user) ).read() )
	Nsimjobs_total = int( os.popen( "echo $(squeue | grep -c 'simProd')"                     ).read() )
	Njobs_user     = int( os.popen( "echo $(squeue  | grep -c '{0}')".format(user)           ).read() )
	Npendjobs_user = int( os.popen( "echo $(squeue -u {0} | grep -c 'PD')".format(user)      ).read() )
	
	now = datetime.now()
	hour = now.hour
	
	#conditions
	time          = hour in allowed_time
	simjobs_total = Options['nsimjobs'] < Nsimjobs_total     
	simjobs_user  = Options['nsimuserjobs'] < Nsimjobs_user  
	jobs_user     = Options['nuserjobs'] < Njobs_user        
	pendjobs_user = Options['npendingjobs'] < Npendjobs_user
							
	if not time:
		print( red("Jobs are sent between {0}h and {1}h!".format(ti, tf)) )
		Submission = False
	elif simjobs_user:
		print( red("You have already submitted {0} simulation jobs. Wait for submission!".format(Nsimjobs_user)) )
		Submission = False
	elif simjobs_total:
		print( red("{0} simulation jobs are submitted. Wait for submission!".format(Nsimjobs_total)) )
		Submission = False
	elif jobs_user:
		print( red("You have already submitted {0} jobs. Wait for submission!".format(Njobs_user)) )
		Submission = False
	elif pendjobs_user:
		print( red("You have already {0} jobs pending. Wait for submission!".format(Npendjobs_user)) )
		Submission = False
	elif time and not simjobs_user and not simjobs_total and not jobs_user and not pendjobs_user:
		Submission = True
				
	return Submission
	
