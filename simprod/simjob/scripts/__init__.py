#!/usr/bin/python

from .GetEvtType import getevttype
from .utils import * 
from .Status import *
from .MoveJobs import *
from .ScreenUtils import *
import os
import subprocess

def IsSlurm():
	
	### Slurm
	try:
		P = subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
def IsLSF():
	
	### LSF
	try:
		P = subprocess.Popen(['bjobs'], stdout=subprocess.PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
def IsHTCondor():
	
	### HTCondor
	
	command = ["which condor_q"]
	
	if sys.version_info[0] > 2:
		process = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')
	else:
		process = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
	time.sleep(0.03)
	out, _ = process.communicate()
	
#	out = os.popen("which condor_q").read()
	
	if "condor_q" in out:
		return True
	else:
		return False
		
		
if IsSlurm():
	from .SlurmUtils import *
	
elif IsHTCondor():
	from .HTCondorUtils import *
	
elif IsLSF():
	from .LSFUtils import *



