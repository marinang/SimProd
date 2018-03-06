#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: addtionnal submission conditon for slurm batch user

from subprocess import Popen, PIPE
from datetime import datetime
import os
import getpass
from .utils import *

def IsLSF():
	
	### Slurm
	try:
		P = Popen(['bjobs'], stdout=PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
def GetLSFStatus( ID ):
	
	ntries = 20
	n = 0
	while n < ntries:
		process  = Popen(["bjobs", "-o", "stat", str(ID)], stdout=PIPE)
		out, _ = process.communicate()
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
	
	
