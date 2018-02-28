#!/usr/bin/python
import argparse
import glob
import os
from pyparsing import *
import shutil
import time

jobdir = os.getenv("SIMOUTPUT")
if jobdir is None :
	jobdir = os.getenv("HOME")+"/SimulationJobs"
	
def MoveFinishedJobs( Path, Options ):
	
	Completed = []
	
	def IsFinished( Directory ):
		
		def DeltaT( time_event ):
			#time_event in second
			now = time.time()
			deltat = (now - time_event) / 3600
			return deltat
			#in hour
		
		files = glob.glob(Directory+"/*")
		
		mtime = max([ os.path.getmtime(f) for f in files ])
		
		if DeltaT( mtime ) > 0.20 :
			return True
		else:
			return False
	
	def IsCompleted( DST, nEvents ):

		if os.path.isfile( DST ) and os.path.getsize( DST ) > 1000000:
			return True
		else:
			return False
			
	def IsCompleted_1( Directory ):
		
		def getstatus( status, line ):
			line = line.replace( status + ":", "")
			line = line.replace( " ", "")
			line = line.replace( "\n", "")
			
			if line == "True":
				return True
			elif line == "False":
				return False
			
		status_file = "{0}/status".format( Directory )
		
		if os.path.isfile( status_file ):
			
			status_file = open( status_file, "r")
			status = status_file.readlines()

			submitted = getstatus("submitted", status[0])
			running   = getstatus("running",   status[1])
			completed = getstatus("completed", status[2])
			failed    = getstatus("failed",    status[3])
			
			return submitted and not running and completed and not failed
			
		else:
			return False
			
	number     = Word(nums+".")
	text       = Word(alphas+nums) 
	underscore = Literal("_") 

	expr = number.setResultsName("year") + Suppress(underscore) + text.setResultsName("polarity") + Suppress(underscore) + number.setResultsName("nevents") + Suppress(text) 
	expr += Suppress(underscore) + Suppress(Literal("s")) + text.setResultsName("stripping") + Suppress(underscore) + text.setResultsName("runnumber")
	
	directories = glob.glob(Path + "{0}_*".format( Options.year ) )
	
	for d in directories:
		
		subjobdir = d.replace( Path, "")
		parsed = expr.parseString(subjobdir)
		
		nEvents = parsed.nevents
		
		dst = "{0}/{1}_events.dst".format( d, nEvents )
		
		xml = d + "/GeneratorLog.xml"
			
		if ( IsCompleted( dst, parsed.nevents ) and IsFinished( d ) ) or IsCompleted_1( d ):
			newdst  = "{0}evts_s{1}_{2}.dst".format( parsed.nevents, parsed.stripping, parsed.runnumber )
			newxml  = "{0}.xml".format( parsed.runnumber )
			
			print(dst)
			
			shutil.move( dst, "{0}/{1}/{2}/{3}/{4}/{5}".format( jobdir, Options.evttype, Options.year, Options.simcond, parsed.polarity, newdst ) )
			shutil.move( xml, "{0}/{1}/{2}/{3}/{4}/xml/{5}".format( jobdir, Options.evttype, Options.year, Options.simcond, parsed.polarity, newxml ) )
			
			os.system("rm -rf " + d)
			
	
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('year',           metavar='<year>',          help="Year to simulate.", type=int, choices=[2011,2012,2015,2016,2017])
	parser.add_argument('--simcond',      metavar='<simcond>',       help="Simulation condition.", default='Sim09c', choices=['Sim09b','Sim09c','Sim09c_LLP','Sim09c_HNL'])
	
	opts = parser.parse_args()
	evttype = opts.evttype
	simcond = opts.simcond
	year    = opts.year
	
	jobspath = jobdir + "/simProd_{0}_{1}/".format( evttype, simcond )
	
	os.system("mkdir -p {0}/{1}/{2}/{3}/MagUp/xml".format( jobdir, evttype, year, simcond))
	os.system("mkdir -p {0}/{1}/{2}/{3}/MagDown/xml".format( jobdir, evttype, year, simcond))
	
	MoveFinishedJobs( jobspath, opts)

	
	