#!/usr/bin/env python

import os
from sys import version_info

def can_mkdir(folder):
	
	try:
		os.mkdir(folder)
		return True
	except OSError:
		
		folders = folder.split("/")
	
		if folders[0] == "":
			folders.remove("")
			folders[0] = "/"+folders[0]
								
		_folders = []
		for i in range(len(folders)):
			_f = folders[0]
			for j in range(1,i+1):
				_f += "/"+folders[j]
			_folders.append(_f)
		folders = _folders

		exist = [os.path.isdir(p) for p in folders ]
				
		for i,(f,e) in enumerate(zip(folders, exist)):
			
			if e == False:
				try:
					os.mkdir(f)
				except OSError:
					print "{0} not a valid path! Permission denied!".format(f)
					return False
					break
				
		return True
				

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
	_input = input
else:
	_input = raw_input

HOME = os.environ['HOME']

if os.path.isfile("{0}/.simprodrc".format(HOME)):
	os.remove("{0}/.simprodrc".format(HOME))

simprodrc = open( "{0}/.simprodrc".format(HOME), "w")
simprodrc.write("\n")

print "\n##### Setting up Simulation Production! #####\n"

print "Choose a destination folder for the simulation jobs!"

valid_path = False
while valid_path == False:
	
	path = _input("path:")
	
	valid_path = can_mkdir(path)

simprodrc.write("SIMOUTPUT={0}\n".format( path ))

simprodrc.close()

print "\nDone.\n"
