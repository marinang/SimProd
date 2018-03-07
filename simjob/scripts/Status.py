#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: get status of jobs for the current submission

import glob
import os
from .utils import *
import time
import subprocess

def GetStatus( Job ):
	
	JobID = Job["jobid"]
	
	### Slurm
	try:
		subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
	except OSError:
		Slurm = False
	else:
		Slurm = True
	
	if Slurm:
		
		ntries = 20
		n = 0
		while n < ntries:
			process  = subprocess.Popen(['sacct','-j', str(JobID), '--format=State'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = process.communicate()
			status = out.split("\n")[-2].replace(" ","").lower()
			
			if status == '----------':
				time.sleep(0.5)
			else:
				break
		
		if status == '----------':
			raise NotImplementedError("Job not found")
				
		return status
						
	elif "lxplus" in os.getenv("HOSTNAME"):
		return NotImplemented
		
					
def SetStatus ( Jobs ):
	
	nthisjob  = Jobs['nthisjob']
	njobs     = Jobs['njobs']
	
	for i in range(nthisjob):
		
		job = Jobs[str(i)]
		
		if job["completed"] or job["failed"]:
			continue

		job["submitted"] = True
			
		IsRunning( job )

		IsCompleted( job )

		IsFailed( job )
		
		WriteStatus( job )
			
			
def WriteStatus ( Job ):
	
	JobDirectory = Job["production_folder"]
	
	status_file = "{0}/status".format(JobDirectory)
	
	if os.path.isfile( status_file ):
		os.remove( status_file )
		
	status_file = open(status_file, "w")
	status_file.write("submitted: {0}\n".format( Job["submitted"] ) )
	status_file.write("running: {0}\n".format( Job["running"] ) )
	status_file.write("completed: {0}\n".format( Job["completed"] ) )
	status_file.write("failed: {0}\n".format( Job["failed"] ) )
	status_file.close()
								
def IsRunning( Job ):
	
	if Job["submitted"]:
		if GetStatus( Job ) == "running":
			Job["running"] = True
		else:
			Job["running"] = False
		
def IsCompleted( Job ):
	
	if Job["submitted"] and IsFinished( Job ):
		JobDirectory = Job["production_folder"]
		
		if os.path.isdir( JobDirectory ):
			dst = JobDirectory + "/" + Job["production_file"]
				
			if os.path.isfile( dst ) and os.path.getsize( dst ) > 1000000:
				Job["completed"] = True
		
		elif IsMoved( Job ):
			Job["completed"] = True
		
def IsFailed( Job ):
	
	if Job["submitted"] and IsFinished( Job ):
		JobDirectory = Job["production_folder"]
		
		if os.path.isdir( JobDirectory ):
			dst = JobDirectory + "/" + Job["production_file"]
		
			if os.path.isfile( dst ) and os.path.getsize( dst ) < 1000000:
				Job["failed"] = True
			elif not os.path.isfile( dst ):
				Job["failed"] = True
				
def IsFinished( Job ):
	
	if Job["submitted"] and not Job["completed"] and not Job["failed"]:
		completed = GetStatus( Job ) == "completed"
		canceled  = GetStatus( Job ) == "canceled"
		failed    = GetStatus( Job ) == "failed"
		
		if completed or canceled or failed:
			return True
		else:
			return False
		
def IsMoved( Job ):
	
	JobDirectory = Job["production_folder"]
	Destination  = Job["destination_folder"]
	File         = Destination + "/" + Job["destination_file"]
		
	if os.path.isdir( JobDirectory ):
		return False
	else:
		if  os.path.isfile( File ):
			return True
		else:
			raise(NotImplementedError("File is lost!"))
		
def Status( Jobs ):
	
	def count( Jobs, status ):
		n = 0
		for i in range( Jobs["njobs"] ):
			if Jobs[str(i)][status]:
				n += 1
		return n
			
	SetStatus( Jobs )
	nrunning   = count( Jobs, "running")
	ncompleted = count( Jobs, "completed")
	nfailed    = count( Jobs, "failed")
		
	print( blue( "{nthisjob}/{njobs} jobs submitted!".format( **Jobs )  ) )
	print( cyan( "{0} jobs running!".format( nrunning ) ) )
	print( green( "{0} jobs completed!".format( ncompleted ) ) )
	print( magenta( "{0} jobs failed!".format( nfailed ) ) )