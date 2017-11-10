#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: addtionnal submission conditon for slurm batch user

from random import randint
from time import sleep
from datetime import datetime
import os
import getpass

def SubCondition( Options ):
	
	user = getpass.getuser()
	
	#additionnal submission condtions for SLURM batch system 
		
	ti, tf = Options.subtime[0], Options.subtime[1]
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
		simjobs_total = Options.nsimjobs < Nsimjobs_total     and Options.nsimjobs != -1
		simjobs_user  = Options.nsimuserjobs < Nsimjobs_user  and Options.nsimuserjobs != -1
		jobs_user     = Options.nuserjobs < Njobs_user        and Options.nuserjobs != -1
		pendjobs_user = Options.npendingjobs < Npendjobs_user and Options.npendingjobs != -1
					
		if not time:
			print( "Jobs are sent between {0}h and {1}h!".format(ti, tf) )
			sleep( randint(0,60) * 60 )
			continue
		elif simjobs_user:
			print( "You have already submitted {0} simulation jobs. Wait for submission!".format(Nsimjobs_user) )
			sleep( randint(0,60) * 60 )
			continue
		elif simjobs_total:
			print( "{0} simulation jobs are submitted. Wait for submission!".format(Nsimjobs_total) )
			sleep( randint(0,60) * 60 )
			continue
		elif jobs_user:
			print( "You have already submitted {0} jobs. Wait for submission!".format(Njobs_user) )
			sleep( randint(0,60) * 60 )
			continue
		elif pendjobs_user:
			print( "You have already {0} jobs pending. Wait for submission!".format(Npendjobs_user) )
			sleep( randint(0,60) * 60 )
			continue
		elif time and not simjobs_user and not simjobs_total and not jobs_user and not pendjobs_user:
			Submission = True
				
	return Submission
