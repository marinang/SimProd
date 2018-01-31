#!/usr/bin/python

import Sim09c
import Sim09b

Sim09b_path = Sim09b.__file__.replace( "pyc", "py" ).replace( "/__init__.py", "" )
Sim09c_path = Sim09c.__file__.replace( "pyc", "py" ).replace( "/__init__.py", "" )

def DoProd( SimCond, Year ):
	
	doprod = "DoProd{0}.sh".format( Year )
	
	if SimCond == "Sim09b":
		doprod = "{0}/{1}".format( Sim09b_path, doprod ) 
		
	if SimCond == "Sim09c":
		doprod = "{0}/{1}".format( Sim09c_path, doprod )
		
	return doprod