#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, getpass

modulepath = None
os.environ["SIMPRODPATH"] = modulepath

simoutput = None
if simoutput is None :
	simoutput = os.getenv("HOME")+"/SimulationJobs"
os.system("mkdir -p "+simoutput)
os.environ["SIMOUTPUT"] = simoutput

#_log_simoutput_ = None
#_if log_simoutput is None :
#_	user = getpass.getuser()
#_	log_simoutput = "/afs/cern.ch/work/{0}/{1}".format( user[0], user )
#_os.system("mkdir -p "+log_simoutput)
#_os.environ["LOG_SIMOUTPUT"] = log_simoutput

import argparse
from simprod import *
from IPython import start_ipython
from traitlets.config.loader import Config

if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('--evttype',      metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('--nevents',      metavar='<nevents>',       help="Number of events to produce.", type=int)
	parser.add_argument('--year',         metavar='<year>',          help="Year to simulate.", type=int, choices=[2011,2012,2015,2016,2017])
	parser.add_argument('--polarity',     metavar='<polarity>',      help="Magnet conditions to simulate.", choices=['MagUp','MagDown'])
	parser.add_argument('--simcond',      metavar='<simcond>',       help="Simulation condition.", default='Sim09c', choices=['Sim09b','Sim09c'])
	parser.add_argument('--stripping',    metavar='<stripping>',     help="Version of the stripping.", type=str)
	parser.add_argument('--turbo',                                   help="Do the Turbo step.", action='store_true')
	parser.add_argument('--mudst',                                   help="Create a muDST output instead of DST ouptut.", action='store_true')  
	parser.add_argument('--neventsjob',   metavar='<neventsjob>',    help="Number of events per job.", type=int, default=50)
	parser.add_argument('--runnumber',    metavar='<runnumber>',     help="Run number for Gauss.", type=int, default=baserunnumber())
	parser.add_argument('--decfiles',     metavar='<decfiles>',      help="Version of the DecFiles package.", type=str, default='v30r5')
	parser.add_argument('--infiles',      metavar='<infiles>',       help="External files to provide for generation, i.e LHE or HepMC files.", type=str, default='')
	
	parser.add_argument('--cpu',          metavar='<cpu>',           help="Number of CPUs per simulation job.", type=int)
			
	#options to control slurm job submission #
	#ideally you would run with these options in a screen session #
	parser.add_argument('--time',         metavar='<time>',          help="(Slurm option) Maximum running time per simulation job in hours.", type=int, default=16)
	parser.add_argument('--nsimjobs',     metavar='<nsimjobs>',      help="(Slurm option) Maximum number of simultaneous simulation jobs running.", type=int)
	parser.add_argument('--nsimuserjobs', metavar='<nsimuserjobs>',  help="(Slurm option) Maximum number of simultaneous simulation jobs running for the user.", type=int)
	parser.add_argument('--nuserjobs',    metavar='<nuserjobs>',     help="(Slurm option) Maximum number of simultaneous jobs running for the user.", type=int)
	parser.add_argument('--npendingjobs', metavar='<npendingjobs>',  help="(Slurm option) Maximum number of pending jobs for the user.", type=int)
	parser.add_argument('--nfreenodes',   metavar='<nfreenodes>',    help="(Slurm option) Number of nodes to be free of user's simulation jobs.", type=int)
	parser.add_argument('--subtime',      metavar='<subtime>',       help="(Slurm option) Time interval when the jobs are sent.", nargs='+', type=int, default=[0, 23])
	
	parser.add_argument('--noui',                                    help="No user interface.", action='store_true') 
	parser.add_argument('--inscreen',                                help="In screen session.", action='store_true')
	parser.add_argument('--keeplogs',                                help="Keep logs in production dir.", action='store_false')  
	
	opts = parser.parse_args()
	
	banner1  = '\n\n'
	banner1 += green(' Welcome on the mini LHCb simulation production framework!\n')
	banner1 += '\n'
	banner1 += green(' author: Matthieu Marinangeli, matthieu.marinangeli@cern.ch.\n')
	
	banner2  = 'production directory: {0}\n'.format(simoutput)

	config = Config()
	
	if opts.evttype and opts.year and opts.nevents:
		if not opts.noui:
			print(banner1)
			print(banner2)
		
		_opts = vars(opts).copy()
		_opts["basedir"] = simoutput
		Jobs = SimulationJob( **_opts )
		Jobs.prepare()
		Jobs.send()
		
		config.TerminalInteractiveShell.banner1 = ""
		config.TerminalInteractiveShell.banner2 = ""
	
	else:
		config.TerminalInteractiveShell.banner1 = banner1
		config.TerminalInteractiveShell.banner2 = banner2
		
	if not opts.noui:
		
		jobs = JobCollection()
		
		_vars = globals().copy()
		_vars.update( locals() )

		start_ipython ( argv = [] , user_ns = _vars, config= config )
		print(blue("\n\t Bye Bye.\n"))
		
		jobs._store_collection()
	