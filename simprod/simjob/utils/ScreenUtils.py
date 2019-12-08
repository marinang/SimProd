#!/usr/bin/python
## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch

import os, time
from .dependencies import LazyModule

screenutils = LazyModule("screenutils")

def SendInScreen(screename, py_file):
	
	s = screenutils.Screen(screename, True )
	
	time.sleep(1)
	
	f = open(py_file, "r")
	old_py_file = f.read()
	f.close()
	
	f = open(py_file, "w")
	f.write(old_py_file)
	f.write("from screenutils import Screen\n")
	f.write("s = Screen('{0}')\n".format(screename))
	f.write("if s.exists:\n".format(screename))
	f.write("\ts.kill()\n".format(screename))
	f.close()
	
	s.send_commands("python {0}".format(py_file))
	
	return s.id
		
def OpenScreenSession(screename):	

	s = screenutils.Screen( screename, True )

	os.system("screen -r {0}".format(s.id) )
	
def KillScreenSession(screename):	
	
	s = screenutils.Screen( screename )
	if s.exists:
		s.kill()
	
def ScreenExist(screename):
	
	s = screenutils.Screen( screename )
	
	return s.exists
	
