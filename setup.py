#!/usr/bin/env python

import os, sys, getpass
from subprocess import Popen, PIPE

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install
from setuptools import Command

modulepath = os.path.dirname(os.path.realpath(__file__))

py3 = sys.version_info[0] > 2 #creates boolean value for test that Python major version > 2


def _input( question, default_answer = None ):

	if py3:
		func = input
	else:
		func = raw_input
		
	result = func(question) or default_answer
	
	return result
			
			
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
			
			
def testcommand(cmd):
	try:
		P = Popen([cmd], stdout=PIPE)
		_, _ = P.communicate()
	except OSError:
		return False
	else:
		return True
		
IsSlurm = lambda: testcommand('squeue')
IsHTCondor = lambda: testcommand('condor_version')
			
					
def pathprint():
	
	print("\n\t- Press ENTER to confirm the location")
	print("\t- Press CTRL-C to abort the installation")
	print("\t- Or specify a different location below\n")
				
install_list = [ 'ipython>=5.0,<6.0;python_version<="2.7"', 
			     'ipython>=5.0;python_version>="3.4"',
			     'screenutils',
			     'tqdm',
			     'colorama',
			     'tinydb>=v3.12.1']
			
if IsHTCondor():
	install_list.append("htcondor")
			
dependency = []

user = getpass.getuser()
			
class PostInstallSetting(install):
	"""Post-installation for installation mode."""
	def run(self):
			
		print("\n##### Setting up Simulation Production! #####\n")
		
		basesimprod = open( "./simprod/scripts/base_simprod.py", "r")
		_basesimprod = basesimprod.read()
		basesimprod.close()
		
		_basesimprod = _basesimprod.replace("modulepath = None","modulepath = '{0}'".format(modulepath))
		
		if "lxplus" in os.getenv("HOSTNAME"):
			
			print("Recommandation for productions in lxplus is to produce the jobs in the EOS space and to have the stdout and stderr stored in AFS WORK!\n")
			print("Do you agree with that?\n")
			
			valid_answer = False
			while valid_answer == False:
				answer = _input("[yes/no]:")
								
				if answer in ["yes","no"]:
					valid_answer = True
				else:
					valid_answer = False
					
			if answer == "yes":
				
				eospath = "/eos/lhcb/user/{0}/{1}/SimulationJobs".format( user[0], user )
				
				print("\nJobs will produced at this location:")
				print(eospath)
				pathprint()
						
				valid_path = False
				while valid_path == False:
					eospath = _input("[{0}] >>> ".format(eospath),eospath)
					valid_path = canmkdir(eospath)
					
				_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(eospath))
				
				workpath = "/afs/cern.ch/work/{0}/{1}/SimulationJobs".format( user[0], user )
					
				print("\nStdout and stderr of the jobs will be stored at this location:")
				print(workpath)
				pathprint()
				
				valid_path = False
				while valid_path == False:
					workpath = _input("[{0}] >>> ".format(workpath),workpath)
					valid_path = canmkdir(workpath)
					
				_basesimprod = _basesimprod.replace("#_","")
				_basesimprod = _basesimprod.replace("log_simoutput_ = None","log_simoutput = '{0}'".format(workpath))
				
			elif answer == "no":
				
				prodpath = "/eos/lhcb/user/{0}/{1}/SimulationJobs".format( user[0], user )
				
				print("\nJobs will produced at this location:")
				print(prodpath)
				pathprint()
				
				valid_path = False
				while valid_path == False:
					prodpath = _input("[{0}] >>> ".format(prodpath),prodpath)
					valid_path = canmkdir(prodpath)
					
				_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(prodpath))
				
		elif "lphe" in os.getenv("HOSTNAME"):
			
				prodpath = "/panfs/{0}/SimulationJobs".format( user )
				
				print("\nJobs will produced at this location:")
				print(prodpath)
				pathprint()
				
				valid_path = False
				while valid_path == False:
					prodpath = _input("[{0}] >>> ".format(prodpath),prodpath)
					valid_path = canmkdir(prodpath)
					
				_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(prodpath))
			
			
		else:
			print("Choose a destination folder for the simulation jobs!")
			
			valid_path = False
			while valid_path == False:
				prodpath = _input("path:")
				valid_path = canmkdir(prodpath)
				
			_basesimprod = _basesimprod.replace("simoutput = None","simoutput = '{0}'".format(prodpath))
			
		simprod = open( "./simprod/scripts/simprod", "w")
		simprod.write(_basesimprod)
		simprod.close()
			
		print("\nDone.\n")
					
		caller = sys._getframe(2)
		caller_module = caller.f_globals.get('__name__','')
		caller_name = caller.f_code.co_name
			
		if caller_module != 'distutils.dist' or caller_name!='run_commands':
			# We weren't called from the command line or setup(), so we
			# should run in backward-compatibility mode to support bdist_*
			# commands.
			install.run(self)
		else:
			self.do_egg_install()

		os.system("rm -rf ./simprod.egg-info")


setup(name = 'simprod',
	  version = '1.0',
	  packages = find_packages(),
	  scripts = ['./simprod/scripts/simprod'],
	  description = 'Mini framework to send LHCb simulation jobs into lxplus or a slurm batch system (with access to cvmfs)!',
	  author = 'Matthieu Marinangeli',
	  author_email = 'matthieu.marinangeli@cern.ch',
	  maintainer = 'Matthieu Marinangeli',
	  maintainer_email = 'matthieu.marinangeli@cern.ch',
	  url = 'https://github.com/marinang/SimulationProduction',
	  install_requires = install_list, 
	  dependency_links = dependency,
	  license = 'GPL-3.0',
	  classifiers=[
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3.4',
			'Programming Language :: Python :: 3.5',
			'Programming Language :: Python :: 3.6',
			'Programming Language :: Python :: 3.7',
	  ],
	  platforms = 'Any',
	  cmdclass={ 'install': PostInstallSetting}
	  )
	  
