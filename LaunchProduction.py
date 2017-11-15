#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: produce simulation samples using lxplus or slurm batch system

import argparse
import os
from datetime import datetime
import subprocess
from random import shuffle
import sys

now = datetime.now()
base_runnumber = (now.minute + 100*now.hour + 10000*now.day + 100000*now.month) * 1000

jobdir = os.getenv("SIMOUTPUT")
if jobdir is None :
	jobdir = os.getenv("HOME")+"/SimulationJobs"
os.system("mkdir -p "+jobdir)

pwd = os.getenv("PWD")
sys.path.append( "{0}/scripts/".format(pwd) )	

def CheckSimInputs( Options ):
	
	if Options.simcond == "Sim09b" and ( Options.year == 2011 or Options.year == 2017 ):
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(Options.year, Options.simcond) )
	elif Options.simcond == "Sim09c" and ( Options.year == 2012 or Options.year == 2017 ):
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(Options.year, Options.simcond) )
	elif Options.turbo and ( Options.year == 2012 or Options.year == 2011 ):
		raise NotImplementedError( "Turbo is not implemented for {0}!".format(Options.year) )
	
def CheckSubmission( Options ):
	
	### Slurm
	try:
		subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
	except OSError:
		Slurm = False
	else:
		Slurm = True

	if (Options.nsimjobs != -1 or Options.nsimuserjobs != -1 or Options.nuserjobs != -1 or  Options.npendingjobs != -1 \
			or  Options.subtime != [0, 23] or Options.nfreenodes != 0 ) and not Slurm:	
		raise NotImplementedError( "These inputs were designed for Slurm batch submission so please don't use them!" )
	
	if Slurm:
		from SlurmSubCondition import SubCondition
		SubCondition( Options )
								 			
def SendJob(EvtType, Year, Polarity, SimCond, Turbo, muDST, Nevents, RunNumber, JobOptions):
		
	OptFile = "{0}/EvtTypes/{1}/{1}.py".format( pwd, EvtType )

	if not os.path.isfile( OptFile ):
		import GetEvtType
		GetEvtType.get(EvtType)
			
	runcmd =  "python scripts/submit.py"
	runcmd += " -D {0}".format( jobdir )
	runcmd += " -d simProd_{0}_{1}".format( EvtType, SimCond)
	if Turbo:
		runcmd += "_Turbo"
	if muDST:
		runcmd += "_muDST"
	runcmd += " -n {0}_{1}_{2}evts -r {3}".format( Year, Polarity, Nevents, RunNumber )     
	runcmd += " 'setup/{0}/DoProd{1}.sh {2} {3} {4} {5} {6} {7}'".format( SimCond, Year, OptFile, Nevents, Polarity, RunNumber, Turbo, muDST )
	runcmd += " -exclude {0}".format( JobOptions.nfreenodes )
	runcmd += " --uexe"
	
	subprocess.call( runcmd, shell=True )
	
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('nevents',        metavar='<nevents>',       help="Number of events to produce.", type=int)
	parser.add_argument('year',           metavar='<year>',          help="Year to simulate.", type=int, choices=[2011,2012,2015,2016,2017])
	parser.add_argument('--polarity',     metavar='<polarity>',      help="Magnet conditions to simulate.", default='', choices=['MagUp','MagDown'])
	parser.add_argument('--simcond',      metavar='<simcond>',       help="Simulation condition.", default='Sim09b', choices=['Sim09b','Sim09c'])
	parser.add_argument('--turbo',                                   help="Do the Turbo step.", action='store_true')
	parser.add_argument('--mudst',                                   help="Create a muDST output instead of DST ouptut.", action='store_true')  
	parser.add_argument('--neventsjobs',  metavar='<neventsjobs>',   help="Number of events per jobs.", type=int, default=50)
	parser.add_argument('--runnumber',    metavar='<runnumber>',     help="Run number for Gauss.", type=int, default=base_runnumber)
			
	#options to control slurm job submission #
	#ideally you would run with these options in a screen session #
	parser.add_argument('--nsimjobs',     metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running.", type=int, default=-1)
	parser.add_argument('--nsimuserjobs', metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running for the user.", type=int, default=-1)
	parser.add_argument('--nuserjobs',    metavar='<nuserjobs>',     help="(Slurm option) Maximum number of simultaneous jobs running for the user.", type=int, default=-1)
	parser.add_argument('--npendingjobs', metavar='<npendingjobs>',  help="(Slurm option) Maximum number of pending jobs for the user.", type=int, default=-1)
	parser.add_argument('--nfreenodes',   metavar='<nfreenodes>',    help="(Slurm option) Number of nodes to be free of user's simulation jobs.", type=int, default=0)
	parser.add_argument('--subtime',      metavar='<subtime>',       help="(Slurm option) Time interval when the jobs are sent.", nargs='+', type=int, default=[0, 23])

	opts = parser.parse_args()
	
	CheckSimInputs( opts )
		
	#Number of jobs
	Njobs = int( opts.nevents/ opts.neventsjobs )
	
	if opts.polarity == '':
		polarity = ["MagUp" for i in range(0,int(Njobs / 2))]
		polarity += ["MagDown" for i in range(int(Njobs / 2), Njobs)]
		shuffle(polarity)
	else:
		polarity = [opts.polarity for i in range(0, opts.nevents)]
				
	for i in range(Njobs):
		
		#Check if ok to submit for slurm batch jobs
		CheckSubmission( opts )
		
		SendJob( opts.evttype, opts.year, polarity[i], opts.simcond, opts.turbo, opts.mudst, opts.neventsjobs, opts.runnumber + i, opts )
						

				
							
						
