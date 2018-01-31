#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: addtionnal submission conditon for slurm batch user

from random import randint
from time import sleep
from datetime import datetime
import os
import getpass
from utils import *
import glob

def GetStatus( Options ):
	
	jobdir = os.getenv("SIMOUTPUT")
	if jobdir is None :
		jobdir = os.getenv("HOME")+"/SimulationJobs"
	
	nthisjob  = Options['nthisjob']
	njobs     = Options['njobs']
	runnumber = Options['runnumber']
	runnumbers = [ runnumber - n for n in range(1,nthisjob) ]
	
	basejobpath = "{0}/simProd_{evttype}_{simcond}/{year}_*_{neventsjob}evts_s{stripping}".format( jobdir, **Options )
	jobpaths = []
	for r in runnumbers:
		jobpaths.append( glob.glob("{0}_{1}".format( basejobpath, r))[0] )
	
	def SubmittedJobs( Options ):
		return blue( "{0}/{njobs} jobs submitted!".format( nthisjob-1, **Options ) )
		
	def CompletedJobs( Options ):
		ncompleted = 0
		
		for p in jobpaths:
			dst = p+"/{neventsjob}_events.dst".format( **Options )
			if os.path.isfile(dst) and os.path.getsize( dst ) > 1000000:
				ncompleted += 1
				
		return green( "{0} jobs completed!".format( ncompleted ) )
			
	def FailedJobs( Options ):
		nfailed = 0	
		
		for p in jobpaths:
			dst = glob.glob( p + "/*events.dst")
			if dst == []:
				continue
				
			dst = p+"/{neventsjob}_events.dst".format( **Options )
			if not os.path.isfile(dst) or os.path.getsize( dst ) < 1000000:
				nfailed += 1
				
		return magenta( "{0} jobs failed!".format( nfailed ) )

	print SubmittedJobs( Options )
	print CompletedJobs( Options )
	print FailedJobs( Options )
	

def SubCondition( Options ):
	
	user = getpass.getuser()

	#additionnal submission conditions for SLURM batch system 
		
	ti, tf = Options['subtime'][0], Options['subtime'][1]
	if ti < tf:
		allowed_time = range(ti,tf+1)
	elif tf < ti:
		allowed_time = range(ti,24) + range(0,tf+1)
			
	Submission = False

	while Submission == False:
		
		Nsimjobs_user  = int( os.popen( "echo $(squeue -u {0} | grep -c 'simProd')".format(user) ).read() )
		Nsimjobs_total = int( os.popen( "echo $(squeue | grep -c 'simProd')"                     ).read() )
		Njobs_user     = int( os.popen( "echo $(squeue  | grep -c '{0}')".format(user)           ).read() )
		Npendjobs_user = int( os.popen( "echo $(squeue -u {0} | grep -c 'PD')".format(user)      ).read() )
		
		now = datetime.now()
		hour = now.hour
		
		#conditions
		time          = hour in allowed_time
		simjobs_total = Options['nsimjobs'] < Nsimjobs_total     and Options['nsimjobs'] != -1
		simjobs_user  = Options['nsimuserjobs'] < Nsimjobs_user  and Options['nsimuserjobs'] != -1
		jobs_user     = Options['nuserjobs'] < Njobs_user        and Options['nuserjobs'] != -1
		pendjobs_user = Options['npendingjobs'] < Npendjobs_user and Options['npendingjobs'] != -1
					
		if not time:
			print( red("Jobs are sent between {0}h and {1}h!".format(ti, tf)) )
			GetStatus( Options )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif simjobs_user:
			print( red("You have already submitted {0} simulation jobs. Wait for submission!".format(Nsimjobs_user)) )
			GetStatus( Options )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif simjobs_total:
			print( red("{0} simulation jobs are submitted. Wait for submission!".format(Nsimjobs_total)) )
			GetStatus( Options )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif jobs_user:
			print( red("You have already submitted {0} jobs. Wait for submission!".format(Njobs_user)) )
			GetStatus( Options )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif pendjobs_user:
			print( red("You have already {0} jobs pending. Wait for submission!".format(Npendjobs_user)) )
			GetStatus( Options )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif time and not simjobs_user and not simjobs_total and not jobs_user and not pendjobs_user:
			Submission = True
				
	return Submission
