#!/usr/bin/env python

import os
from sys import version_info

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install

modulepath = os.path.dirname(os.path.realpath(__file__))

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
	_input = input
else:
	_input = raw_input
	
def canmkdir(folder):
	try:
		os.makedirs(folder)
		return True
	except OSError as e:
		if e.strerror == "File exists":
			return True
		else:
			print(e.message)
			print(e.strerror)
			return False

class PostInstallSetting(install):
	"""Post-installation for installation mode."""
	def run(self):
		
		print("\n##### Setting up Simulation Production! #####\n")
		
		basesimprod = open( "./simprod/scripts/base_simprod.py", "r")
		_basesimprod = basesimprod.read()
		basesimprod.close()
		
		_basesimprod = _basesimprod.replace("modulepath = None","modulepath = '{0}'".format(modulepath))
		
		if "lxplus" in os.getenv("HOSTNAME"):
			
			print("Recommandation for productions in lxplus is to produce the jobs in the AFS WORK space and to direct to the jobs to EOS once finished!\n")
			print("Do you want to produce the jobs in AFS work and send them once completed to EOS?\n")
			
			valid_answer = False
			while valid_answer == False:
				answer = _input("[yes/no]:")
				
				if answer in ["yes","no"]:
					valid_answer = True
				else:
					valid_answer = False
					
			if answer == "yes":
				print("\nChoose a production folder for the simulation jobs! (/afs/cern.ch/work/...)")
				
				valid_path = False
				while valid_path == False:
					prodpath = _input("path:")
					valid_path = canmkdir(prodpath)
					
				_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(prodpath))
					
				print("\nChoose a destination folder for the simulation jobs! (/eos/lhcb/user/...)")
				
				valid_path = False
				while valid_path == False:
					eospath = _input("path:")
					valid_path = canmkdir(eospath)
					
				_basesimprod = _basesimprod.replace("#_","")
				_basesimprod = _basesimprod.replace("eos_simoutput_ = None","eos_simoutput = '{0}'".format(eospath))
				
			elif answer == "no":
				print("Choose a destination folder for the simulation jobs!")
				
				valid_path = False
				while valid_path == False:
					prodpath = _input("path:")
					valid_path = canmkdir(prodpath)
					
				_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(prodpath))
			
		else:
			print("Choose a destination folder for the simulation jobs!")
			
			valid_path = False
			while valid_path == False:
				prodpath = _input("path:")
				valid_path = canmkdir(prodpath)
				
			_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(prodpath))
			
		simprod = open( "./bin/simprod", "w")
		simprod.write(_basesimprod)
		simprod.close()
			
		print("\nDone.\n")
		
		install.run(self)


setup(name = 'simprod',
	  version = '1.0',
	  packages = find_packages(),
	  scripts = ['bin/simprod'],
	  description = 'Mini framework to send LHCb simulation jobs into lxplus or a slurm batch system (with access to cvmfs)!',
	  author = 'Matthieu Marinangeli',
	  author_email = 'matthieu.marinangeli@cern.ch',
	  maintainer = 'Matthieu Marinangeli',
	  maintainer_email = 'matthieu.marinangeli@cern.ch',
	  url = 'https://github.com/marinang/SimulationProduction',
	  install_requires = ['pyparsing>=2.1.9', 'ipython>=3.2.1' ], 
	  classifiers=[
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3.4',
			'Programming Language :: Python :: 3.5',
			'Programming Language :: Python :: 3.6',
			'Programming Language :: Python :: 3.7',
	  ],
	  platforms = 'Any',
	  cmdclass={ 'install': PostInstallSetting },
	  )
	  
