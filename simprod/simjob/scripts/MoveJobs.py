#!/usr/bin/python

import os, shutil

def Move( initial_file, destination_file ):
	
	destination_dir = os.path.dirname(destination_file)
	
	if not os.path.isdir(destination_dir):
		os.system("mkdir -p {0}".format(destination_dir))
		
	shutil.move( initial_file, destination_file )
	
def EosMove( initial_file, destination_file ):
	
	destination_dir = os.path.dirname(destination_file)
	
	if not os.path.isdir(destination_dir):
		os.system("xrdfs root://eoslhcb.cern.ch/ mkdir -p {0}".format( destination_dir ))
		
	os.system("xrdfs root://eoslhcb.cern.ch/ mv {0} {1}".format( initial_file, destination_file ))