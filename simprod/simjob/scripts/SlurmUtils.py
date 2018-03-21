#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: addtionnal submission conditon for slurm batch user

from subprocess import Popen, PIPE
from datetime import datetime
import os
import getpass
from .utils import *
import time
import sys

def KillSlurm( ID ):
	
	kill = Popen(['scancel',str(ID)], stdout=PIPE, stderr=PIPE)
	_, _ = kill.communicate()


def IsSlurm():
	
	### Slurm
	try:
		P = Popen(['squeue'], stdout=PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
def GetSlurmStatus( ID ):
	
	ntries = 20
	n = 0
	while n < ntries:
		if sys.version_info[0] > 2:
			process  = Popen(['sacct','-j', str(ID), '--format=State'], stdout=PIPE, encoding='utf8')
		else:
			process  = Popen(['sacct','-j', str(ID), '--format=State'], stdout=PIPE)
		out, _ = process.communicate()
		status = out.split("\n")[-2].replace(" ","").lower()
		
		if status == '----------':
			time.sleep(0.5)
		else:
			break
	
	if status == '----------':
		status = "notfound"
		
	return status
	
	
def DefaultSlurmOptions( ):
	
	now     = datetime.now()
	hour    = now.hour
	weekday = now.weekday()
	
	### During the day less job submission
	
	options = {}	
	
	if hour > 6 and hour < 22:
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
		
	options["nsimjobs"]     = nsimjobs
	options["nsimuserjobs"] = nsimuserjobs
	options["nuserjobs"]    = nuserjobs
	options["npendingjobs"] = npendingjobs
	options["nfreenodes"]   = nfreenodes
	options["cpu"]          = 4140
		
	return options	
		
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
