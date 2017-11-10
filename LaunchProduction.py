#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: produce simulation samples using slurm batch system

import argparse
import os
import getpass
from datetime import datetime
import subprocess
import GetEvtType
from random import shuffle

now = datetime.now()
base_runnumber = (now.minute + 100*now.hour + 10000*now.day + 100000*now.month) * 1000

user = getpass.getuser()

jobdir = os.getenv("SIMOUTPUT")
if jobdir is None :
	jobdir = os.getenv("HOME")+"/SimulationJobs/"
os.system("mkdir -p "+jobdir)

pwd = os.getenv("PWD")
	
	
def CheckSubmission( Options ):
	
	### Slurm
	try:
		subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
	except OSError:
		Slurm = True
	else:
		Slurm = False
		
	if Options.nsimjobs != -1 and Options.nsimuserjobs != -1 and Options.nuserjobs != -1 and  Options.npendingjobs != -1 \
			and Options.subtime != [0, 23] and not Slurm:	
		raise NotImplementedError( "These inputs were designed for slurm batch submission so please don't use them!" )
	
	if Slurm:
		from scripts.SlurmSubCondition import SubCondition
		SubCondition( Options )
	
						 			
def SendJob(EvtType, Year, Polarity, Nevents, RunNumber):
		
	OptFile = "{0}/EvtTypes/{1}/{1}.py".format( pwd, EvtType )

	if not os.path.isfile( OptFile ):
		
		GetEvtType.get(EvtType)
			
	runcmd =  "python scripts/submit.py"
	runcmd += " -D {0}".format( jobdir )  
	runcmd += " -d simProd_{0} -n {2}_{3}_{1}evts -r {4}".format( EvtType, Nevents, Year, Polarity, RunNumber )     
	runcmd += " 'scripts/DoProd{0}.sh {1} {2} {3} {4}'".format( Year, OptFile, Nevents, Polarity, RunNumber )
	runcmd += " --uexe"
	
	subprocess.call( runcmd, shell=True )
	
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('nevents',        metavar='<nevents>',       help="Number of events to produce.", type=int)
	parser.add_argument('year',           metavar='<year>',          help="Year to simulate.", type=int, choices=[2012,2015,2016])
	parser.add_argument('--polarity',     metavar='<polarity>',      help="Magnet conditions to simulate.", default='', choices=['MagUp','MagDown']) 
	parser.add_argument('--neventsjobs',  metavar='<neventsjobs>',   help="Number of events per jobs.", type=int, default=50)
	parser.add_argument('--runnumber',    metavar='<runnumber>',     help="Run number for Gauss.", type=int, default=base_runnumber)
			
	#options to control slurm job submission #
	#ideally you would run with these options in a screen session #
	parser.add_argument('--nsimjobs',     metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running.", type=int, default=-1)
	parser.add_argument('--nsimuserjobs', metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running for the user.", type=int, default=-1)
	parser.add_argument('--nuserjobs',    metavar='<nuserjobs>',     help="(Slurm option) Maximum number of simultaneous jobs running for the user.", type=int, default=-1)
	parser.add_argument('--npendingjobs', metavar='<npendingjobs>',  help="(Slurm option) Maximum number of pending jobs for the user.", type=int, default=-1)
	parser.add_argument('--subtime',      metavar='<subtime>',       help="(Slurm option) Time interval when the jobs are sent.", nargs='+', type=int, default=[0, 23])
		
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
		
		#Check if ok to submit for slurm batch jobs
		CheckSubmission( opts )
		
		SendJob( opts.evttype, opts.year, polarity[i], opts.neventsjobs, opts.runnumber + i )
						

				
							
						