#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: copy the all options files related to an EvtType in a directory called EvtTypes.
## The users can they modify as they want these options files.

import argparse
import os
import shutil
import sys

decfiles_path = '/cvmfs/lhcb.cern.ch/lib/lhcb/DBASE/Gen/DecFiles/v30r5'

pwd = os.getenv("PWD")

def get(EvtType):
	
	optfile = "{0}/options/{1}.py".format( decfiles_path ,EvtType )
	
	if not os.path.isfile( optfile ):
		sys.exit("This Evttype does not exist !")
	
	os.system( "mkdir -p EvtTypes" )
	os.system( "mkdir -p EvtTypes/{0}".format(EvtType) )	
			
	with open(optfile, 'r') as file:
		lines = file.readlines()
		
	decfileroot_files = [] 	
		
	for i,l in enumerate(lines):
		if "DECFILESROOT" in l:
				decfile         = l.split("DECFILESROOT")[-1]
				decfile         = decfile.split('"')[0] 
				decfile         = decfile.replace( '"\n', '' )
				decfileroot_files.append({"file":decfile, "index":i})
				
	for f in decfileroot_files:
		filename = f["file"].split('/')[-1]
		index = f["index"]
		shutil.copyfile( "{0}/{1}".format( decfiles_path , f["file"] ), "{0}/EvtTypes/{1}/{2}".format( pwd, EvtType, filename ) )
		
		#modify the locations in the option file		
		lines[index] = lines[index].replace( "$DECFILESROOT{0}".format(f["file"]) , "{0}/EvtTypes/{1}/{2}".format( pwd, EvtType, filename ) )
	
	OptFile = "{0}/EvtTypes/{1}/{1}.py".format( pwd, EvtType )
	
	with open(OptFile, 'w') as file:
			file.writelines( lines )
				
				
if __name__ == "__main__" :

	parser = argparse.ArgumentParser(description='')
	
	parser.add_argument('evttype',        metavar='<evttype>',       help="EvtType of the processus to generate.", type=str)
	
	opts = parser.parse_args()			
				
	get( opts.evttype )	
				
