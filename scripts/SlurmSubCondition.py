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
from Status import Status

def SetDefaultSlurmOptions( Options ):
	
	now     = datetime.now()
	hour    = now.hour
	weekday = now.weekday()
	
	### During the day less job submission	
	
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
		

	if Options["nsimjobs"]     is None:
		Options["nsimjobs"]     = nsimjobs
	if Options["nsimuserjobs"] is None:	
		Options["nsimuserjobs"] = nsimuserjobs
	if Options["nuserjobs"]    is None:
		Options["nuserjobs"]    = nuserjobs
	if Options["npendingjobs"] is None:
		Options["npendingjobs"] = npendingjobs
	if Options["nfreenodes"]   is None:
		Options["nfreenodes"]   = nfreenodes
	
def SubCondition( Options ):
	
	SetDefaultSlurmOptions( Options )
	
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
		simjobs_total = Options['nsimjobs'] < Nsimjobs_total     
		simjobs_user  = Options['nsimuserjobs'] < Nsimjobs_user  
		jobs_user     = Options['nuserjobs'] < Njobs_user        
		pendjobs_user = Options['npendingjobs'] < Npendjobs_user
				
		atpreviousjobs = Options.copy()
		atpreviousjobs['runnumber'] = Options['runnumber'] - 1
		atpreviousjobs['nthisjob']  = Options['nthisjob'] - 1
					
		if not time:
			print( red("Jobs are sent between {0}h and {1}h!".format(ti, tf)) )
			Status( atpreviousjobs )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif simjobs_user:
			print( red("You have already submitted {0} simulation jobs. Wait for submission!".format(Nsimjobs_user)) )
			Status( atpreviousjobs )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif simjobs_total:
			print( red("{0} simulation jobs are submitted. Wait for submission!".format(Nsimjobs_total)) )
			Status( atpreviousjobs )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif jobs_user:
			print( red("You have already submitted {0} jobs. Wait for submission!".format(Njobs_user)) )
			Status( atpreviousjobs )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif pendjobs_user:
			print( red("You have already {0} jobs pending. Wait for submission!".format(Npendjobs_user)) )
			Status( atpreviousjobs )
			print( "\n" )
			sleep( randint(0,30) * 60 )
			continue
		elif time and not simjobs_user and not simjobs_total and not jobs_user and not pendjobs_user:
			Submission = True
				
	return Submission
