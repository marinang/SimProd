#!/usr/bin/python

import os
import glob

sim_path = os.getenv("SIMPRODPATH")+"/simprod/simjob/setup/"
Sim09c_path = os.getenv("SIMPRODPATH")+"/simprod/simjob/setup/Sim09c"
Sim09c_path = os.getenv("SIMPRODPATH")+"/simprod/simjob/setup/Sim09c"

def DoProd( SimCond, Year ):
	
	doprod = "DoProd{0}.sh".format( Year )
	
	paths = glob.glob(sim_path + "*")
	
	simconds = [p.split("/")[-1] for p in paths]
	
	if SimCond in simconds:
		doprod = "{0}/{1}".format( sim_path + SimCond, doprod ) 
		return doprod
	else:
		raise ValueError("...")
				