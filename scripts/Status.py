#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: get status of jobs for the current submission

import glob
import os
from utils import *

def JobPaths( Options ):
	
	nthisjob  = Options['nthisjob']
	njobs     = Options['njobs']
	runnumber = Options['runnumber']
	runnumbers = [ runnumber - n for n in range(0,nthisjob) ]
	
	jobdir = os.getenv("SIMOUTPUT")
	if jobdir is None :
		jobdir = os.getenv("HOME")+"/SimulationJobs"
			
	basejobpath = "{0}/simProd_{evttype}_{simcond}/{year}_*_{neventsjob}evts_s{stripping}".format( jobdir, **Options )
	jobpaths = []
	for r in runnumbers:
		jobpaths.append( glob.glob("{0}_{1}".format( basejobpath, r))[0] )
		
	return jobpaths

def SubmittedJobs( Options ):
		return  "{0}/{njobs} jobs submitted!".format( nthisjob, **Options )
		
def CompletedJobs( Options ):
	ncompleted = 0
	
	for p in JobPaths( Options ):
		dst = p+"/{neventsjob}_events.dst".format( **Options )
		if os.path.isfile(dst) and os.path.getsize( dst ) > 1000000:
			ncompleted += 1
			
	return ncompleted  
	
def FailedJobs( Options ):
	nfailed = 0	
	
	for p in JobPaths( Options ):
		dst = glob.glob( p + "/*events.dst")
		if dst == []:
			continue
			
		dst = p+"/{neventsjob}_events.dst".format( **Options )
		if not os.path.isfile(dst) or os.path.getsize( dst ) < 1000000:
			nfailed += 1
			
	return nfailed

def Status( Options ):
		
	print blue( SubmittedJobs( Options )  )
	print green( "{0} jobs completed!".format( CompletedJobs( Options ) ) )
	print magenta( "{0} jobs failed!".format( FailedJobs( Options ) ) )