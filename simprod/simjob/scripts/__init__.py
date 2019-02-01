#!/usr/bin/python

from .GetEvtType import getevttype
from .utils import * 
from .Status import *
from .MoveJobs import *
from .ScreenUtils import *
import os

def IsSlurm():
	
	### Slurm
	try:
		P = Popen(['squeue'], stdout=PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
def IsLSF():
	
	### LSF
	try:
		P = Popen(['bjobs'], stdout=PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
def IsHTCondor():
	
	### HTCondor
	
	out = os.popen("which condor_q").read()
	
	if "condor_q" in out:
		return True
	else:
		return False
#	
#	
#	try:
#		P = Popen(['condor_q'], stdout=PIPE)
#		_, _ = P.communicate()
#	except OSError:
#		return False
#	else:
#		return True
		
if IsSlurm():
	from .SlurmUtils import *
	
elif IsHTCondor():
	from .HTCondorUtils import *
	
elif IsLSF():
	from .LSFUtils import *



