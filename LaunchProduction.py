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
			
def CheckSubmission( Jobs ):
	
	### Slurm
	try:
		subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
	except OSError:
		Slurm = False
	else:
		Slurm = True
	
	if Slurm:
		SubCondition( Jobs )
		
def PrepareJobs( Options, **kwargs ):
		
	#Number of jobs
	Njobs = int( opts.nevents/ opts.neventsjob )
	
	jobs = {"njobs": Njobs}
	
	if  Njobs == 0:
		warnings.warn( red(" WARNING: no jobs are being sent (make sure that neventsjob is smaller than nevents)! "), stacklevel = 2 )
	
	if Options.polarity == '':
		polarity = ["MagUp" for i in range(0,int(Njobs / 2))]
		polarity += ["MagDown" for i in range(int(Njobs / 2), Njobs)]
		shuffle(polarity)
	else:
		polarity = [Options.polarity for i in range(0, Njobs)]
		
	options = vars(Options).copy()	
	options.pop( 'polarity',  None )
	options.pop( 'runnumber', None )
	options.pop( 'infiles',   None )
	
	OptFile = "{0}/EvtTypes/{evttype}/{evttype}.py".format( pwd, **options )
	
	if not os.path.isfile( OptFile ):
		GetEvtType.get( **options )
		
	options["options_file"] = OptFile
		
	ext = "dst"	
	subdir = 'simProd_{evttype}_{simcond}'.format( **options)
	if options['turbo']:
		subdir += "_Turbo"
	if options['mudst']:
		subdir += "_muDST"
		ext     = "mdst"
		
	options["subdir"] = subdir		
	options["jobdir"] = jobdir
	
	jobs["options"] = options
			
	for n in range(Njobs):
		
		_polarity  = polarity[n]
		_runnumber = opts.runnumber + n
			
		opts_n = {}
		opts_n['runnumber'] = _runnumber
		opts_n['polarity']  = _polarity
		opts_n['infiles']   = ""
		opts_n['submitted'] = False
		opts_n['running']   = False
		opts_n['completed'] = False
		opts_n['failed']    = False
			
		jobname = '{year}_{0}_{neventsjob}evts_s{stripping}_{1}'.format( _polarity, _runnumber, **options )
		opts_n["jobname"]            = jobname
		opts_n["jobid"]              = ""
		opts_n["production_folder"]  = "{0}/{1}/{2}".format( jobdir, subdir, jobname )
		opts_n["production_file"]    = "{neventsjob}_events.{0}".format( ext, **options )
		opts_n["destination_folder"] = "{0}/{evttype}/{year}/{simcond}/{1}".format( jobdir, _polarity, **options )
		opts_n["destination_file"]   = "{neventsjob}evts_s{stripping}_{0}.{1}".format( _runnumber, ext, **options )
		
		jobs[str(n)] = opts_n
			
	return jobs
		
def SendJobs( Jobs ):
	
	for i in range( Jobs['njobs'] ):
		SendJob( Jobs, i)
			
def SendJob( Jobs, Jobnumber ):
		
	from setup import DoProd
	
	Jobs["nthisjob"] = Jobnumber
	CheckSubmission( Jobs )
	
	job     = Jobs[str(Jobnumber)]
	options = Jobs["options"].copy()
	options.update(job)
	
	doprod  = DoProd( options['simcond'], options['year'])

	command = '{0} {options_file} {neventsjob} {polarity} {runnumber} {turbo} {mudst} {stripping}'.format( doprod, **options )

	batchoptions = {"basedir": options['jobdir'], "subdir": options['subdir'], "jobname": options['jobname'], "command": command, 
					"exclude": options['nfreenodes'], "cpu": options['cpu'], "time": options['time'], "unique": True, 
					'infiles': job['infiles'], 'thisjob': job }
								
	submit( **batchoptions )
	time.sleep(0.5)
	print blue( "{0}/{1} jobs submitted!".format( Jobnumber+1, Jobs['njobs'] ) )
	
					
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

	jobs = PrepareJobs( opts )
		
	SendJobs( jobs )
		
		
		
						

				
							
						
