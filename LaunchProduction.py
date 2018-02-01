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
import warnings
from scripts import *

now = datetime.now()
base_runnumber = (now.minute + 100*now.hour + 10000*now.day + 1000000*now.month) * 100

jobdir = os.getenv("SIMOUTPUT")
if jobdir is None :
	jobdir = os.getenv("HOME")+"/SimulationJobs"
os.system("mkdir -p "+jobdir)


def CheckSimInputs( Options ):
	
	def StrippingVersion( Options ,*args ):
		args = list(args)
		with warnings.catch_warnings():
			warnings.simplefilter("always")	
			if Options.stripping == "":
				Options.stripping = args[0]
				if len(args) > 1:
					warnings.warn( red("Default stripping verion {0} used. {1} versions are available.".format( Options.stripping, args)), stacklevel = 2)
			elif Options.stripping not in args:
				raise NotImplementedError( "Stripping version {0} is not available for {1} {2}! Only {3}!".format(Options.stripping, Options.year, Options.simcond, args) )	
					
	if Options.simcond == "Sim09b" and ( Options.year == 2011 or Options.year == 2017 ):
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(Options.year, Options.simcond) )
		
	elif Options.simcond == "Sim09c" and Options.year == 2017:
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(Options.year, Options.simcond) )
	
	if Options.year == 2012:
		if Options.simcond == "Sim09b":
			StrippingVersion(Options, "21")
		elif Options.simcond == "Sim09c":
			StrippingVersion(Options, "21")
		
	elif Options.year == 2015:
		if Options.simcond == "Sim09b":
			StrippingVersion(Options, "24")
		if Options.simcond == "Sim09c":
			StrippingVersion(Options, "24r1", "24r1p1")
		
	elif Options.year == 2016:
		if Options.simcond == "Sim09b":
			StrippingVersion(Options, "28")
		if Options.simcond == "Sim09c":
			StrippingVersion(Options, "28r1", "28r1p1")	
							
	if Options.mudst and ( Options.year == 2012 or Options.year == 2011 ):
		raise NotImplementedError( "No micro DST output for {0}!".format(Options.year) )
			
	if Options.turbo and ( Options.year == 2012 or Options.year == 2011 ):
		raise NotImplementedError( "Turbo is not implemented for {0}!".format(Options.year) )
		
	
def CheckSubmission( Options ):
	
	### Slurm
	try:
		subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
	except OSError:
		Slurm = False
	else:
		Slurm = True
	
	if Slurm:
		SubCondition( Options )
								 			
def SendJob( Options ):
	
	from setup import DoProd
		
	OptFile = "{0}/EvtTypes/{evttype}/{evttype}.py".format( pwd, **Options )

	if not os.path.isfile( OptFile ):
		GetEvtType.get( Options )
		
	subdir = 'simProd_{evttype}_{simcond}'.format( **Options )
	if Options['turbo']:
		subdir += "_Turbo"
	if Options['mudst']:
		subdir += "_muDST"
		
	jobname = '{year}_{polarity}_{neventsjob}evts_s{stripping}'.format( **Options )
	
	doprod  = DoProd( Options['simcond'], Options['year'])

	command = '{0} {1} {neventsjob} {polarity} {runnumber} {turbo} {mudst} {stripping}'.format( doprod, OptFile, **Options )
	
	infiles = Options['infiles'].split()
		
	batchoptions = {"basedir": jobdir, "subdir":subdir, "jobname":jobname, "command": command, 
					"run": Options['runnumber'], "exclude": Options['nfreenodes'], "cpu": Options['cpu'], 
					"time": Options['time'], "unique":True, 'infiles':infiles }
					
	submit( **batchoptions )
				
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('nevents',        metavar='<nevents>',       help="Number of events to produce.", type=int)
	parser.add_argument('year',           metavar='<year>',          help="Year to simulate.", type=int, choices=[2011,2012,2015,2016,2017])
	parser.add_argument('--polarity',     metavar='<polarity>',      help="Magnet conditions to simulate.", default='', choices=['MagUp','MagDown'])
	parser.add_argument('--simcond',      metavar='<simcond>',       help="Simulation condition.", default='Sim09b', choices=['Sim09b','Sim09c'])
	parser.add_argument('--stripping',    metavar='<stripping>',     help="Version of the stripping.", type=str, default='')
	parser.add_argument('--turbo',                                   help="Do the Turbo step.", action='store_true')
	parser.add_argument('--mudst',                                   help="Create a muDST output instead of DST ouptut.", action='store_true')  
	parser.add_argument('--neventsjob',   metavar='<neventsjob>',    help="Number of events per job.", type=int, default=50)
	parser.add_argument('--runnumber',    metavar='<runnumber>',     help="Run number for Gauss.", type=int, default=base_runnumber)
	parser.add_argument('--decfiles',     metavar='<decfiles>',      help="Version of the DecFiles package.", type=str, default='v30r5')
	parser.add_argument('--infiles',      metavar='<infiles>',       help="External files to provide for generation, i.e LHE or HepMC files.", type=str, default='')
			
	#options to control slurm job submission #
	#ideally you would run with these options in a screen session #
	parser.add_argument('--cpu',          metavar='<cpu>',           help="(Slurm option) Number of CPUs per simulation job.", type=int, default=4000)
	parser.add_argument('--time',         metavar='<time>',          help="(Slurm option) Maximum running time per simulation job in hours.", type=int, default=10)
	parser.add_argument('--nsimjobs',     metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running.", type=int, default=400)
	parser.add_argument('--nsimuserjobs', metavar='<nsimuserjobs>',  help="(Slurm option) Maximum number of simultaneous simulation jobs running for the user.", type=int, default=100)
	parser.add_argument('--nuserjobs',    metavar='<nuserjobs>',     help="(Slurm option) Maximum number of simultaneous jobs running for the user.", type=int, default=150)
	parser.add_argument('--npendingjobs', metavar='<npendingjobs>',  help="(Slurm option) Maximum number of pending jobs for the user.", type=int, default=40)
	parser.add_argument('--nfreenodes',   metavar='<nfreenodes>',    help="(Slurm option) Number of nodes to be free of user's simulation jobs.", type=int, default=4)
	parser.add_argument('--subtime',      metavar='<subtime>',       help="(Slurm option) Time interval when the jobs are sent.", nargs='+', type=int, default=[0, 23])

	opts = parser.parse_args()
		
	CheckSimInputs( opts )
	
	#Number of jobs
	Njobs = int( opts.nevents/ opts.neventsjob )
	
	if  Njobs == 0:
		warnings.warn( red(" WARNING: no jobs are being sent (make sure that neventsjob is smaller than nevents)! "), stacklevel = 2 )
	
	if opts.polarity == '':
		polarity = ["MagUp" for i in range(0,int(Njobs / 2))]
		polarity += ["MagDown" for i in range(int(Njobs / 2), Njobs)]
		shuffle(polarity)
	else:
		polarity = [opts.polarity for i in range(0, Njobs)]
						
	for i,n in enumerate( range(Njobs) ):
		
		opts_i = vars(opts).copy()
		opts_i['runnumber'] = opts.runnumber + i
		opts_i['polarity']  = polarity[i]
		opts_i['nthisjob']  = n + 1
		opts_i['njobs']     = Njobs
		
		#Check if ok to submit for slurm batch jobs
		CheckSubmission( opts_i )
			
		SendJob( opts_i )
		
		print blue( "{0}/{1} jobs submitted!".format( n + 1, Njobs ) )
		
						

				
							
						
