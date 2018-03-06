#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: simulation job class

from random import shuffle
from scripts import *
import os
import time
from random import randint
from setup import DoProd

				
class JobCollection(object):
	"""
	Class handling submission of jobs
	"""
	
	def __init__(self, **kwargs):
				
		self._jobs    = {}
		self._options = {}
		
		self._evttype    = kwargs.get('evttype', None)
			
		self._nevents    = kwargs.get('nevents', None)
			
		self._neventsjob = kwargs.get('neventsjob', None)
		
		self._year       = kwargs.get('year', None)

		self._polarity   = kwargs.get('polarity', None)
		
		self._simcond    = kwargs.get('simcond', None)
			
		self._stripping  = kwargs.get('stripping', None)
		
		self._turbo      = kwargs.get('turbo', False)
			
		self._mudst      = kwargs.get('mudst', False)
		
		self._runnumber  = kwargs.get('runnumber', baserunnumber())
	
		#Number of jobs
		self._njobs = int( self._nevents/ self._neventsjob )
		
		if  self._njobs  == 0:
			warnings.warn( red(" WARNING: no jobs are being sent (make sure that neventsjob is smaller than nevents)! "), stacklevel = 2 )
					
		if not self._polarity:
			polarity = ["MagUp" for i in range(0,int(self._njobs / 2))]
			polarity += ["MagDown" for i in range(int(self._njobs / 2), self._njobs)]
			shuffle(polarity)
			self._polarity = polarity
		else:
			self._polarity = [self._polarity for i in range(0, self.njobs)]
				
		pwd = os.path.dirname(os.path.realpath(__file__)).replace("simjob","")
				
		self._optfile = "{0}/EvtTypes/{1}/{1}.py".format( pwd, self._evttype )
		
		if not os.path.isfile( self._optfile ):
			GetEvtType.get( kwargs )
			
		_basedir  = kwargs.get('basedir', None)
		if not _basedir:
			raise NotImplementedError('basedir not defined!')
		self._options["basedir"] = _basedir
		self._basedir = self._options["basedir"]
					
		self._ext = "dst"	
		subdir = "simProd_{0}_{1}".format( self._evttype, self._simcond)
		if self._turbo:
			subdir += "_Turbo"
		if self._mudst:
			subdir += "_muDST"
			self._ext     = "mdst"
			
		self._options["subdir"] = subdir
		self._subdir = self._options["subdir"]	
		self._production_folder  = "{0}/{1}".format( self._basedir, self._subdir)
		self._destination_folder = "{0}/{1}/{2}/{3}/{4}".format( self._basedir, self._evttype, self._year, self._simcond, self._polarity)
		self._doprod  = DoProd( self._simcond, self._year )
		
		if IsSlurm():
			
			self._options["lsf"]      = False
			self._lsf                 = self._options["lsf"]
			self._options["slurm"]    = True	
			self._slurm               = self._options["slurm"]
			self._options["cpu"]      = kwargs.get('cpu', None)
			self._options["time"]     = kwargs.get('time', None)
			self._options["subtime"]  = kwargs.get('subtime', None)
						
			default_options    = DefaultSlurmOptions( )
			
			self._options["default_options"] = []
			
			self._options["nsimjobs"]     = kwargs.get('nsimjobs', None)
			if not self._options["nsimjobs"]:
				self._options["nsimjobs"]             = default_options['nsimjobs']
				self._options["default_options"]     += ["nsimjobs"]
				
			self._options["nsimuserjobs"] = kwargs.get('nsimuserjobs', None)
			if not self._options["nsimuserjobs"]:
				self._options["nsimuserjobs"]         = default_options['nsimuserjobs']
				self._options["default_options"]     += ["nsimuserjobs"]
				
			self._options["nuserjobs"]    = kwargs.get('nuserjobs', None)
			if not self._options["nuserjobs"]:
				self._options["nuserjobs"]            = default_options['nuserjobs']
				self._options["default_options"]     += ["nuserjobs"]
				
			self._options["npendingjobs"]  = kwargs.get('npendingjobs', None)
			if not self._options["npendingjobs"]:
				self._options["npendingjobs"]         = default_options['npendingjobs']
				self._options["default_options"]     += ["npendingjobs"]
				
			self._options["nfreenodes"]    = kwargs.get('nfreenodes', None)
			if not self._options["nfreenodes"]:
				self._options["nfreenodes"]           = default_options['nfreenodes']
				self._options["default_options"]     += ["nfreenodes"]
				
		elif IsLSF():
			
			self._options["lsf"]      = True
			self._lsf                 = self._options["lsf"]
			self._options["slurm"]    = False	
			self._slurm               = self._options["slurm"]
			
	@property
	def nevents( self):
		return self._nevents
			
	@property	
	def options( self):
		return self._options
			
	def jobs( self, job_number = None ):
		
		if job_number == None:
			return self._jobs.values()
		else:
			return self._jobs[str(job_number)]
		
	@property
	def status( self):

		nrunning   = 0
		ncompleted = 0 
		nfailed    = 0
		nsubmitted = 0
		
		for j in self.jobs():
			status = j.status
			if status == "submitted":
				nsubmitted += 1
			elif status == "running":
				nrunning   += 1
				nsubmitted += 1
			elif status == "completed":
				ncompleted += 1
				nsubmitted += 1
			elif status == "failed":
				nfailed    += 1
				nsubmitted += 1
		
		print(blue( "{0}/{1} jobs submitted!".format( nsubmitted, self._njobs )  )) 
		print(cyan( "{0} jobs running!".format( nrunning ) )) 
		print(green( "{0} jobs completed!".format( ncompleted ) )) 
		print(magenta( "{0} jobs failed!".format( nfailed ) )) 
										
	def command( self, polarity, runnumber):
		
		doprod  = DoProd( self._simcond, self._year)
		
		command  = doprod
		command += ' {0}'.format( self._optfile)
		command += ' {0}'.format( self._neventsjob)
		command += ' {0}'.format( polarity)
		command += ' {0}'.format( runnumber)
		command += ' {0}'.format( self._turbo)
		command += ' {0}'.format( self._mudst)
		command += ' {0}'.format( self._stripping)
			
		return command
		
	def prepare( self, job_number = None, **kwargs ):
		
		if not self._evttype:
			raise NotImplementedError('Evttype not defined!')
			
		if not self._nevents:
			raise NotImplementedError('nevents not defined!')
			
		if not self._neventsjob:
			raise NotImplementedError('nevents not defined!')
			
		if not self._year:
			raise NotImplementedError('year not defined!')
			
		if not self._simcond:
			raise NotImplementedError('simcond not defined!')
			
		if not self._stripping:
			raise NotImplementedError('stripping not defined!')
		
		infiles = kwargs.get('infiles', [])

		for n in range(self._njobs):
			
			if job_number != None and job_number != n:
				continue
			
			polarity  = self._polarity[n]
			runnumber = self._runnumber + n
	
			options = {"infiles": infiles}
			options["jobname"] = "{0}_{1}_{2}evts_s{3}_{4}".format( self._year, polarity, self._neventsjob, self._stripping, runnumber )
			options["production_file"]  = "{0}/{1}_events.{2}".format( self._production_folder, self._neventsjob, self._ext )
			options["destination_file"] = "{0}/{1}evts_s{2}_{3}.{4}".format( self._destination_folder, self._neventsjob, self._stripping, runnumber, self._ext )
			options["batch_options"] = self.options
			options["batch_command"] = self.command( polarity, runnumber)
					
			self._jobs[str(n)] = SimulationJob( **options )
						
	def cansubmit( self):
		if self._slurm:
			#update default options
			default_options  = DefaultSlurmOptions( )
			for opt in self.options["default_options"]:
				self.options[opt] = default_options[opt]

			return SubCondition( self.options )
		else:
			return True
				
	def send( self, job_number = None ):
		
		for n in range(self._njobs):
			
			if job_number != None and job_number != n:
				continue
		
			SUBMIT = False
			while SUBMIT == False:
				SUBMIT = self.cansubmit()
				if not SUBMIT:
					self.status
					print("")
					time.sleep( randint(0,30) * 60 )
								
			self.jobs(n).send
			time.sleep(0.5)
			print( blue( "{0}/{1} jobs submitted!".format( n+1, self._njobs ) ) )

			
class SimulationJob(object):
	"""
	Class for simulation jobs
	"""
	
	def __init__(self, **kwargs):
		
		self._jobid = None					
		self._infiles = kwargs.get('infiles', [])
		
		if not isinstance(self._infiles, list) and " " in self._infiles:
			self._infiles = self._infiles.split(" ")
		elif not isinstance(self._infiles, list):
			self._infiles = [self._infiles]
		
		self._jobname         = kwargs.get('jobname', None)
		if not self._jobname:
			raise NotImplementedError('jobname not defined!')
		
		self._production_file = kwargs.get('production_file', None)
		if not self._production_file:
			raise NotImplementedError('production file not defined!')
			
		self._destination_file = kwargs.get('destination_file', None)
		if not self._destination_file:
			raise NotImplementedError('destination file not defined!')
			
		self._batch_options    = kwargs.get('batch_options', None)
		if not self._batch_options:
			raise NotImplementedError('batch options not defined!')
		
		self._batch_command    = kwargs.get('batch_command', None)
		if not self._batch_command:
			raise NotImplementedError('batch command not defined!')
			
		self._send_options = self._batch_options.copy()
		self._send_options["jobname"] = self._jobname
		self._send_options["infiles"] = self._infiles
		self._send_options["command"] = self._batch_command
		
		self._submitted = False
		self._running   = False
		self._finished  = False
		self._completed = False
		self._failed    = False
	
	@property	
	def send( self):
		send_options = self._send_options
		self._jobid = submit( **send_options )
		self._submitted = True
			
	@property
	def jobid( self):
		return self._jobid
					
	@property
	def status( self):
		if not self._finished and self._submitted:
			self.updatestatus()
		if self._submitted and not self._running and not self._finished:
			return "submitted"
		elif self._submitted and self._running and not self._finished:
			return "running"
		elif self._submitted and not self._running and self._finished:
			if self._completed:
				return "completed"
			elif self._failed:
				return "failed"
		
	@property
	def output( self):
		if os.path.isfile( self._production_file):
			return self._production_file
		elif os.path.isfile( self._destination_file):
			return self._destination_file
		else:	
			return ""
					
	def updatestatus( self):
		if self._batch_options["slurm"]:
			status = GetSlurmStatus( self.jobid )								
		elif self._batch_options["lsf"]:
			status = GetLSFStatus( self.jobid )
			
		if status == "running" and not self._running:
			self._running = True
			
		if status == "completed" or status == "canceled" or status == "failed":
			self._running  = False
			self._finished = True
			
			if self.output != "" and os.path.isfile( self.output ):
				if os.path.isfile( self.output ) and os.path.getsize( self.output ) > 1000000:
					self._completed = True
				elif os.path.isfile( self.output ) and os.path.getsize( self.output ) < 1000000:
					self._failed = True
			elif self.output == "":
				self._failed = True




			
		
