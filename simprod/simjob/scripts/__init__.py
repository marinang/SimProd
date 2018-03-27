#!/usr/bin/python

from .GetEvtType import *
from .submit import main as submit
from .utils import * 
from .Status import *
from .MoveJobs import *
from .ScreenUtils import *

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
	
	### Slurm
	try:
		P = Popen(['bjobs'], stdout=PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
if IsSlurm():
	from .SlurmUtils import *
	
if IsLSF():
	from .LSFUtils import *



