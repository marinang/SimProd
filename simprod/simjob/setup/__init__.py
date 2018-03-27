#!/usr/bin/python

import os

Sim09b_path = os.getenv("SIMPRODPATH")+"/simprod/simjob/setup/Sim09b"
Sim09c_path = os.getenv("SIMPRODPATH")+"/simprod/simjob/setup/Sim09c"

def DoProd( SimCond, Year ):
	
	doprod = "DoProd{0}.sh".format( Year )
	
	if SimCond == "Sim09b":
		doprod = "{0}/{1}".format( Sim09b_path, doprod ) 
		
	if SimCond == "Sim09c":
		doprod = "{0}/{1}".format( Sim09c_path, doprod )
		
	return doprod