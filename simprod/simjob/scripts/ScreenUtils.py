#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch

import screenutils, os, time

def SendInScreen( screename, py_file ):
	
	s = screenutils.Screen( screename, True )
	
	time.sleep(2)
	
	f = open(py_file, "r")
	old_py_file = f.read()
	
	f = open(py_file, "w")
	f.write(old_py_file)
	f.write("from screenutils import Screen\n")
	f.write("s = Screen('{0}')\n".format(screename))
	f.write("if s.exists:\n".format(screename))
	f.write("\ts.kill()\n".format(screename))
	
	s.send_commands("python {0}".format(py_file))
	
	return s.id
		
def OpenScreenSession( screename ):	

	s = screenutils.Screen( screename, True )

	os.system("screen -r {0}".format(s.id) )
	
def KillScreenSession( screename ):	
	
	s = screenutils.Screen( screename, True )
	
	s.kill()
	
def ScreenExist( screename ):
	
	s = screenutils.Screen( screename )
	
	return s.exists
	
