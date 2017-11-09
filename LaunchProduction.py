#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: produce simulation samples using slurm batch system

import argparse
import os
import getpass
from datetime import datetime
import subprocess
from random import randint, shuffle
from time import sleep
import GetEvtType

now = datetime.now()
base_runnumber = (now.minute + 100*now.hour + 10000*now.day + 100000*now.month) * 1000

user = getpass.getuser()

jobdir = os.getenv("SIMOUTPUT")
if jobdir is None :
	jobdir = os.getenv("HOME")+"/SimulationJobs/"
os.system("mkdir -p "+jobdir)

pwd = os.getenv("PWD")
	
def SubCondition( Options ):
		
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
					 			
def SendJob(EvtType, Year, Polarity, Nevents, RunNumber):
		
	OptFile = "{0}/EvtTypes/{1}/{1}.py".format( pwd, EvtType )

	if not os.path.isfile( OptFile ):
		
		GetEvtType.get(EvtType)
			
	runcmd =  "python scripts/submit.py"
	runcmd += " -D {0}".format( jobdir )  
	runcmd += " -d simProd_{0} -n {2}_{3}_{1}evts -r {4}".format( EvtType, Nevents, Year, Polarity, RunNumber )     
	runcmd += " 'scripts/DoProd{0}.sh {1} {2} {3} {4}'".format( Year, OptFile, Nevents, Polarity, RunNumber )
	runcmd += " -cpu 4000 --uexe"
	
	subprocess.call( runcmd, shell=True )
	
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('nevents',        metavar='<nevents>',       help="Number of events to produce.", type=int)
	parser.add_argument('year',           metavar='<year>',          help="Year to simulate.", type=int, choices=[2012,2015,2016])
	parser.add_argument('--polarity',     metavar='<polarity>',      help="Magnet conditions to simulate.", default='', choices=['MagUp','MagDown']) 
	parser.add_argument('--neventsjobs',  metavar='<neventsjobs>',   help="Number of events per jobs.", type=int, default=50)
	parser.add_argument('--runnumber',    metavar='<runnumber>',     help="Run number for Gauss.", type=int, default=base_runnumber)
	
	#options to control job submission #
	#ideally you would run with these options in a screen session #
	parser.add_argument('--nsimjobs',     metavar='<nsimjobs>',      help="Maximum number of simultaneous simulation jobs running.", type=int, default=-1)
	parser.add_argument('--nsimuserjobs', metavar='<nsimjobs>',      help="Maximum number of simultaneous simulation jobs running for the user.", type=int, default=-1)
	parser.add_argument('--nuserjobs',    metavar='<nuserjobs>',     help="Maximum number of simultaneous jobs running for the user.", type=int, default=-1)
	parser.add_argument('--npendingjobs', metavar='<npendingjobs>',  help="Maximum number of pending jobs for the user.", type=int, default=-1)
	parser.add_argument('--subtime',      metavar='<subtime>',       help="Time interval when the jobs are sent.", nargs='+', type=int, default=[0, 23])
		
	opts = parser.parse_args()
	
	#Number of jobs
	Njobs = int( opts.nevents/ opts.neventsjobs )
	
	if opts.polarity == '':
		polarity = ["MagUp" for i in range(0,int(opts.nevents / 2))]
		polarity += ["MagDown" for i in range(int(opts.nevents / 2), opts.nevents)]
		shuffle(polarity)
	else:
		polarity = [opts.polarity for i in range(0, opts.nevents)]
				
	for i in range(Njobs):
		
		# check if ok to submit
		SubCondition( opts )
		
		SendJob( opts.evttype, opts.year, polarity[i], opts.neventsjobs, opts.runnumber + i )
			

	
				
			