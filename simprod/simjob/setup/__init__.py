#!/usr/bin/python

import os
import glob

#print(os.path.realpath(__file__))
#sim_path = os.getenv("SIMPRODPATH")+"/simprod/simjob/setup/"

sim_path = os.path.realpath(__file__)

def DoProd( SimCond, Year ):
	
	doprod = "DoProd{0}.sh".format( Year )
	
	paths = glob.glob(sim_path + "*")
	
	simconds = [p.split("/")[-1] for p in paths]
	
	if SimCond in simconds:
		doprod = "{0}/{1}".format( sim_path + SimCond, doprod ) 
		return doprod
	else:
		raise ValueError("Error {0} {1} not found.".format(SimCond, Year))
				