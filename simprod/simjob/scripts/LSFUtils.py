#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch

from subprocess import Popen, PIPE
from datetime import datetime
import os
from .utils import *
import sys

def KillLSF( ID ):
	
	kill = Popen(['bkill',str(ID)], stdout=PIPE, stderr=PIPE)
	out, err = kill.communicate()	
		
def DefaultLSFOptions( ):
	
	options = {}		
	options["cpu"]  = 9000
		
	return options
		
def GetLSFStatus( ID ):
	
	if sys.version_info[0] > 2:	
		process  = Popen(["bjobs", "-o", "stat", str(ID)], stdout=PIPE, stderr=PIPE, encoding='utf8')
	else:
		process  = Popen(["bjobs", "-o", "stat", str(ID)], stdout=PIPE, stderr=PIPE)
	out, err = process.communicate()
		
	if err == "Job <{0}> is not found\n".format(ID):
		status = "notfound"
	else:
		status = out.split("\n")[1].replace(" ","").lower()
		if status == "pend":
			status = "pending"
		elif status == "run":
			status = "running"
		elif status == "done":
			status = "completed"
		elif status == "exit" or status == "ususp" or status == "ssusp":
			status = "canceled"
		elif status == "unkwn" or status == "zombi":
			status = "failed"
			
	return status
	
	#### put a try and catch
	
	
