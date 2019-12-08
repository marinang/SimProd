#!/usr/bin/python

import os
import glob
import warnings

from ..utils import red

sim_path = os.path.dirname(__file__)

def DoProd( SimCond, Year ):

	doprod = "DoProd{0}.sh".format( Year )
	
	paths = glob.glob(sim_path + "/*")
	
	simconds = [p.split("/")[-1] for p in paths]
	
	if SimCond in simconds:
		doprod = "{0}/{1}".format( sim_path + SimCond, doprod ) 
		return doprod
	else:
		raise ValueError("Error {0} {1} not found.".format(SimCond, Year))
				
				
def checksiminputs(job):
	
	def StrippingVersion(*args):
		args = list(args)
		with warnings.catch_warnings():
			warnings.simplefilter("always")	
			if job.stripping == None:
				job.stripping = args[0]
				if len(args) > 1:
					warnings.warn( red("Default stripping version {0} used. {1} versions are available.".format( 
									job.stripping, 
								   	args)), 
								   	stacklevel = 2)
			elif job._stripping not in args:
				raise NotImplementedError( "Stripping version {0} is not available for {1} {2}! Only {3}!".format( 
								   	job.stripping, 
								   	job.year, 
								   	job.simcond, 
								   	args) )	
					
	if job.simcond == "Sim09b" and job.year in [2011, 2017, 2018]:
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
									job.year, 
									job.simcond) )
		
	elif job.simcond == "Sim09c" and job.year in [2017, 2018]:
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
									job.year, 
									job.simcond) )
		
	elif job.simcond == "Sim09d" and job.year in [2011, 2012, 2015, 2016, 2017, 2018]:
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
									job.year, 
									job.simcond) )
									
	elif job.simcond == "Sim09e" and job.year in [2011, 2012, 2018]:
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
									job.year, 
									job.simcond) )	
			   
	elif job.simcond == "Sim09g" and job.year in [2011, 2012, 2015]:
		raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
									job.year, 
									job.simcond) )									
	
									
	if job.year == 2011:
		if job.simcond == "Sim09c":
			StrippingVersion("21r1")
	
	if job.year == 2012:
		if job.simcond == "Sim09b":
			StrippingVersion("21")
		elif job.simcond == "Sim09c":
			StrippingVersion("21")
		
	elif job.year == 2015:
		if job.simcond == "Sim09b":
			StrippingVersion("24")
		if job.simcond in ["Sim09c", "Sim09e"]:
			StrippingVersion("24r1", "24r1p1")
		
	elif job.year == 2016:
		if job.simcond == "Sim09b":
			StrippingVersion("28")
		if job.simcond in ["Sim09c", "Sim09e", "Sim09g"]:
			StrippingVersion("28r1", "28r1p1")	
			
	elif job.year == 2017:
		StrippingVersion("29r2")
		
	elif job.year == 2018:
		if job.simcond == "Sim09g":
			StrippingVersion("34", "34r0p1")
		else:
			StrippingVersion("34")
		
	if job.simmodel not in ["pythia8", "BcVegPy"]:
		raise ValueError("simmodel must be pythia8 or BcVegPy!")
	elif job.simmodel == "BcVegPy" and job.simcond not in ["Sim09e", "Sim09g"]:
		raise NotImplementedError("BcVegPy is not implemented for {0}!".format(job.simcond))
		
	if job.redecay and job.simcond == "Sim09b":
		raise NotImplementedError("ReDecay is not implemented for {0}!".format(job.simcond))
							
	if job.mudst and ( job.year == 2012 or job.year == 2011 ):
		raise NotImplementedError("No micro DST output for {0}!".format(job.year))
			
	if job.turbo and ( job.year == 2012 or job.year == 2011 ):
		raise NotImplementedError("Turbo is not implemented for {0}!".format(job.year))
