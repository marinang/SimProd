#!/usr/bin/python
import argparse
import glob
import os
from pyparsing import *
import shutil
import time
from subprocess import Popen, PIPE

jobdir = os.getenv("SIMOUTPUT")
if jobdir is None :
	jobdir = os.getenv("HOME")+"/SimulationJobs"
eosdir = os.getenv("EOS_SIMOUTPUT")

def silentrm( path ):
	
	P = Popen(['rm','-rf',path], stdout=PIPE, stderr=PIPE)
	_, _ = P.communicate()
	
def MoveFinishedJobs( Options ):
	
	if Options["toeos"]:
		dir_ = eosdir
		os.system("xrdfs root://eoslhcb.cern.ch/ mkdir -p {0}/{evttype}/{year}/{simcond}/MagUp/xml".format( dir_, **Options))
		os.system("xrdfs root://eoslhcb.cern.ch/ mkdir -p {0}/{evttype}/{year}/{simcond}/MagDown/xml".format( dir_,**Options))
		proddir_ = jobdir
	else:
		dir_ = jobdir
		os.system("mkdir -p {0}/{evttype}/{year}/{simcond}/MagUp/xml".format( dir_, **Options))
		os.system("mkdir -p {0}/{evttype}/{year}/{simcond}/MagDown/xml".format( dir_,**Options))
	
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
						
	Path = dir_ + "/simProd_{evttype}_{simcond}/".format( **Options )
		
	if Options["toeos"]:
		Path_prod = proddir_ + "/simProd_{evttype}_{simcond}/".format( **Options )
			
	number     = Word(nums+".")
	text       = Word(alphas+nums) 
	underscore = Literal("_") 

	expr = number.setResultsName("year") + Suppress(underscore) + text.setResultsName("polarity") + Suppress(underscore) + number.setResultsName("nevents") + Suppress(text) 
	expr += Suppress(underscore) + Suppress(Literal("s")) + text.setResultsName("stripping") + Suppress(underscore) + text.setResultsName("runnumber")
	
	directories = glob.glob(Path + "{year}_*".format( **Options ) )
	
	for d in directories:
		
		subjobdir = d.replace( Path, "")
		parsed = expr.parseString(subjobdir)
		
		if Options["toeos"]:
			production_dir = Path_prod + subjobdir
						
		if len(os.listdir(d)) < 1:
			silentrm(d)
			if Options["toeos"]:
				silentrm(production_dir)
			continue
				
		nEvents = parsed.nevents
		
		dst = "{0}/{1}_events.dst".format( d, nEvents )
		
		xml = d + "/GeneratorLog.xml"
		
		completed = IsCompleted( dst, parsed.nevents )
		finished  = IsFinished( d )
			
		if completed and finished:
			newdst  = "{0}evts_s{1}_{2}.dst".format( parsed.nevents, parsed.stripping, parsed.runnumber )
			newxml  = "{0}.xml".format( parsed.runnumber )
			
			print(dst)
			
			if Options["toeos"]:
				os.system("xrdfs root://eoslhcb.cern.ch/ mv {0} {1}/{evttype}/{year}/{simcond}/{2}/{3}".format( dst, dir_, parsed.polarity, newdst,  **Options ))
				os.system("xrdfs root://eoslhcb.cern.ch/ mv {0} {1}/{evttype}/{year}/{simcond}/{2}/xml/{3}".format( xml, dir_, parsed.polarity, newxml,  **Options ))
				
				if os.path.isdir(production_dir):
					silentrm(production_dir)
				
			else:
				shutil.move( dst, "{0}/{evttype}/{year}/{simcond}/{1}/{2}".format( dir_, parsed.polarity, newdst, **Options ) )
				shutil.move( xml, "{0}/{{evttype}/{year}/{simcond}/{1}/xml/{2}".format( dir_, parsed.polarity, newxml , **Options ) )
						
			silentrm(d)
			
		elif not completed and finished:
			if os.path.isfile(dst):
				os.remove(dst)
			if os.path.isfile(xml):
				os.remove(xml)
			silentrm(d)
			
			if Options["toeos"] and os.path.isdir(production_dir):
				silentrm(production_dir)
	
	if Options["toeos"]:	
		directories = glob.glob(Path_prod + "{year}_*".format( **Options ) )
		
		for d in directories:
			
			subjobdir = d.replace( Path_prod, "")
			parsed = expr.parseString(subjobdir)
			
			finished  = IsFinished( d )
										
			if len(os.listdir(d)) < 1 or finished:
				silentrm(d)

if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	parser.add_argument('year',           metavar='<year>',          help="Year to simulate.", type=int, choices=[2011,2012,2015,2016,2017])
	parser.add_argument('--simcond',      metavar='<simcond>',       help="Simulation condition.", default='Sim09c', choices=['Sim09b','Sim09c'])
	parser.add_argument('--toeos',                                   help="If jobs were moved to eos.", action='store_true') 
	
	opts = parser.parse_args()
	
	opts = vars(opts).copy()
	
	MoveFinishedJobs( opts )

	
	