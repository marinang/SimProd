#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: get status of jobs for the current submission

import glob
import os
from utils import *
import time

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
		return  "{nthisjob}/{njobs} jobs submitted!".format( **Options )
		
		
def IsFinished( Directory ):
	
	def DeltaT( time_event ):
		#time_event in second
		now = time.time()
		deltat = (now - time_event) / 3600
		return deltat
		#in hour
	
	files = glob.glob(Directory+"/*")
	
	mtime = max([ os.path.getmtime(f) for f in files ])
	
	if DeltaT( mtime ) > 0.20 :
		return True
	else:
		return False
	
		
def CompletedJobs( Options ):
	ncompleted = 0
	
	for p in JobPaths( Options ):
		dst = p+"/{neventsjob}_events.dst".format( **Options )
		if os.path.isfile(dst) and os.path.getsize( dst ) > 1000000 and IsFinished(p):
			ncompleted += 1
			
	return ncompleted
	
def RunningJobs( Options ):
	nrunning = 0
	
	for p in JobPaths( Options ):
		files = glob.glob(p+"/*")
		if len(files) > 5 and not IsFinished(p):
			nrunning += 1
			
	return nrunning   
	
def FailedJobs( Options ):
	nfailed = 0	
	
	for p in JobPaths( Options ):
		dst = p+"/{neventsjob}_events.dst".format( **Options )
		if not os.path.isfile(dst) and IsFinished(p):
			nfailed += 1
		elif os.path.isfile(dst) and os.path.getsize( dst ) < 1000000:
			nfailed += 1
			
	return nfailed

def Status( Options ):
		
	print blue( SubmittedJobs( Options )  )
	print cyan( "{0} jobs running!".format( RunningJobs( Options ) ) )
	print green( "{0} jobs completed!".format( CompletedJobs( Options ) ) )
	print magenta( "{0} jobs failed!".format( FailedJobs( Options ) ) )