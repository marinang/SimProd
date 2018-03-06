#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: produce simulation samples using lxplus or slurm batch system

import argparse
import os
import subprocess
from random import shuffle
import sys
import warnings
from scripts import *
import time
from simjob.simjob import JobCollection

basedir = os.getenv("SIMOUTPUT")
if basedir is None :
	basedir = os.getenv("HOME")+"/SimulationJobs"
os.system("mkdir -p "+basedir)

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
	parser.add_argument('--runnumber',    metavar='<runnumber>',     help="Run number for Gauss.", type=int, default=baserunnumber())
	parser.add_argument('--decfiles',     metavar='<decfiles>',      help="Version of the DecFiles package.", type=str, default='v30r5')
	parser.add_argument('--infiles',      metavar='<infiles>',       help="External files to provide for generation, i.e LHE or HepMC files.", type=str, default='')
			
	#options to control slurm job submission #
	#ideally you would run with these options in a screen session #
	parser.add_argument('--cpu',          metavar='<cpu>',           help="(Slurm option) Number of CPUs per simulation job.", type=int, default=4140)
	parser.add_argument('--time',         metavar='<time>',          help="(Slurm option) Maximum running time per simulation job in hours.", type=int, default=16)
	parser.add_argument('--nsimjobs',     metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running.", type=int)
	parser.add_argument('--nsimuserjobs', metavar='<nsimuserjobs>',  help="(Slurm option) Maximum number of simultaneous simulation jobs running for the user.", type=int)
	parser.add_argument('--nuserjobs',    metavar='<nuserjobs>',     help="(Slurm option) Maximum number of simultaneous jobs running for the user.", type=int)
	parser.add_argument('--npendingjobs', metavar='<npendingjobs>',  help="(Slurm option) Maximum number of pending jobs for the user.", type=int)
	parser.add_argument('--nfreenodes',   metavar='<nfreenodes>',    help="(Slurm option) Number of nodes to be free of user's simulation jobs.", type=int)
	parser.add_argument('--subtime',      metavar='<subtime>',       help="(Slurm option) Time interval when the jobs are sent.", nargs='+', type=int, default=[0, 23])

	opts = parser.parse_args()
	
	# Check simulation inputs
	CheckSimInputs( opts )
	
	opts = vars(opts).copy()
	
	opts["basedir"] = basedir
	
	Jobs = JobCollection( **opts )

	Jobs.prepare()
	
	Jobs.send()
		

		
						

				
							
						
