#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@epfl.ch
## Description: produce simulation samples in the LPHE cluster

import argparse
import os
import random
import getpass
from datetime import datetime
import subprocess
import shutil

now = datetime.now()
random.seed(now.day * 100 + now.hour)
randomrun = (now.minute + 100*now.hour + 10000*now.day + 100000*now.month) * 1000

user = getpass.getuser()
jobdir = '/panfs/{0}/SimulationJobs'.format(user)
os.system( "mkdir -p {0}".format(jobdir) )

pwd = os.environ["PWD"]

def SendJob(EvtType, Year, Polarity, Nevents, RunNumber):
		
	if not os.path.isdir ( "EvtTypes" ):
		os.mkdir ( "EvtTypes" )	
	if not os.path.isdir ( os.path.join( "EvtTypes", EvtType ) ):
		os.mkdir ( os.path.join( "EvtTypes", EvtType ) )
		
	shutil.copyfile( "setup/DecFiles/options/{0}.py".format(EvtType), "EvtTypes/{0}/{0}.py".format(EvtType) )
		
	OptFile = "{0}/EvtTypes/{1}/{1}.py".format( pwd, EvtType )
	
	runcmd =  "python scripts/submit.py"
	runcmd += " -D {0}".format( jobdir )  
	runcmd += " -d simProd_{0} -n {2}_{3}_{1}evts -r {4}".format( EvtType, Nevents, Year, Polarity, RunNumber )     
	runcmd += " 'scripts/DoProd{0}.sh {1} {2} {3} {4}'".format( Year, OptFile, Nevents, Polarity, RunNumber )
	runcmd += " -cpu 4000 --uexe"
	
	print runcmd
	
	subprocess.call(runcmd,shell=True)
	
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',          metavar='<evttype>',        help="EvtType of the processus to generate", type=str)
	parser.add_argument('nevents',          metavar='<nevents>',        help="Number of events to produce", type=int)
	parser.add_argument('year',             metavar='<year>',           help="Year to simulate", type=int, choices=[2015,2016])
	parser.add_argument('--polarity',       metavar='<polarity>',       help="Magnet conditions to simulate", default='', choices=['MagUp','MagDown']) 
	parser.add_argument('--neventsjobs',    metavar='<neventsjobs>',    help="Number of events per jobs", type=int, default=50) 
	
	opts = parser.parse_args()
	
	Njobs = int( opts.nevents/ opts.neventsjobs )
	
	for i in range(Njobs):
		
		runnumber = randomrun + i
		
		SendJob( opts.evttype, opts.year, opts.polarity, opts.neventsjobs, runnumber )
		