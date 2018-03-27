#!/usr/bin/python
# -*- coding: utf-8 -*-

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: simulation job class

from random import shuffle
from .scripts import *
import os
import time
from random import randint
from .setup import DoProd
import warnings
import glob
import json


class JobCollection(object):
	"""
	Simulation job collection.
	"""
	
	def __init__(self, **kwargs):
		self._jobs     = {}	
		self._jsondict = {}	
		
		simprod = os.getenv("SIMPRODPATH")+"/simprod"		
		self._jobsdir   = "{0}/._simjobs_".format(simprod)
		self._collection_file = "{0}/collection.json".format(self._jobsdir)

		if os.path.isfile( self._collection_file ):
			_collectedjobs = json.load(open(self._collection_file))
			self._jsondict = _collectedjobs
			
			for cj in _collectedjobs.keys():
				if not os.path.isfile(_collectedjobs[cj]):
					continue
				self._jobs[cj]     = SimulationJob().from_file(_collectedjobs[cj])
				self._jsondict[cj] = _collectedjobs[cj]
				
		self.__update()
								
	def _keys(self):
		_keys = [int(k) for k in self._jobs.keys()]
		return sorted(_keys, key=int)
			
	def __str__(self):
		self.__update()
		
		toprint  = "{0} jobs\n".format(len(self._jobs))
		
		h_job     = "    #job "
		h_status  = "       status "
		h_evttype = "       evttype "
		h_year    = "   year "
		h_nevents = "  #events "
		h_subjobs = "  #subjobs "
		
		header = "{0}|{1}|{2}|{3}|{4}|{5}|\n".format( 
					h_job, 
					h_status, 
					h_evttype, 
					h_year, 
					h_nevents, 
					h_subjobs)
					
		line = "-"*(len(header) - 2) + "\n"
				
		toprint += line
		toprint += header
		toprint += line
	
		for i in self._keys():
			
			job     = self._jobs[str(i)]
			status  = job.status
			evttype = job.evttype
			year    = job.year
			nevents = job.nevents
			subjobs = job.nsubjobs
			
			if status == "submitted":
				color = cyan
			elif status == "new":
				color = cdefault
			elif status == "submitting":
				color = magenta
			elif status == "running":
				color = green
			elif status == "completed":
				color = blue
			elif status == "failed":
				color = red
								
			p_job     = "{n:{fill}{al}{w}} ".format(w=(len(h_job)-1), al='>', fill='', n=i)
						
			p_status  = "{n:{fill}{al}{w}} ".format(w=(len(h_status)-1), al='>', fill='', n=status)
			
			p_evttype = "{n:{fill}{al}{w}} ".format(w=(len(h_evttype)-1), al='>', fill='', n=evttype)
			
			p_year    = "{n:{fill}{al}{w}} ".format(w=(len(h_year)-1), al='>', fill='', n=year)
			
			p_nevents = "{n:{fill}{al}{w}} ".format(w=(len(h_nevents)-1), al='>', fill='', n=nevents)
			
			p_subjobs = "{n:{fill}{al}{w}} ".format(w=(len(h_subjobs)-1), al='>', fill='', n=subjobs)
						
			toprint += color("{0}|{1}|{2}|{3}|{4}|{5}|\n".format( 
						p_job, 
						p_status, 
						p_evttype, 
						p_year, 
						p_nevents, 
						p_subjobs))
	
		return toprint
		
	def _repr_pretty_(self, p, cycle):
		if cycle:
			p.text('job collection...')
			return
		p.text(self.__str__())
		
	def __getitem__(self, i):
		if i not in self._keys():
			self.__update()
		if i not in self._keys():
			raise ValueError("jobs({0}) not found!".format(i))
		else:
			return self._jobs[str(i)]
			
	def __update(self):
		jsonfiles = glob.glob("{0}/*_*_*_*_*.json".format(self._jobsdir))
		
		for k in self._jsondict.keys():
			_file = self._jsondict[k]
			if not os.path.isfile(_file):
				self._jsondict.pop(k, None)
				self._jobs.pop(k, None)

			elif self._jobs[str(k)].status == "new":
				self._jobs[str(k)] = SimulationJob().from_file(_file)
				
		for js in jsonfiles:
			if js not in self._jsondict.values():
				if len(self._jsondict) < 1:
					index = 0
				else:
					maxindex = max(self._keys())
					index    = str(maxindex + 1) 
				self._jobs[str(index)] = SimulationJob().from_file(js) 
				self._jsondict[str(index)] = js
				
		self._store_collection()
							
	def _store_collection(self):
				
		if not os.path.isdir(self._jobsdir):
			os.system("mkdir -p {0}".format(self._jobsdir))
								
		jsondict = json.dumps(self._jsondict)
		f = open(self._collection_file, "w")
		f.write(jsondict)
		f.close()
		
#		for i in self._keys():
#			job = self._jobs[str(i)]		
#		job._store_job()		
				
class SimulationJob(object):
	"""
	Simulation job
	"""
	
	def __init__(self, **kwargs):			
		self._subjobs = {}
		self._options = {}
					
		self._nevents    = kwargs.get('nevents', None)
		self._neventsjob = kwargs.get('neventsjob', 50)
		self._year       = kwargs.get('year', None)
		self._polarity   = kwargs.get('polarity', None)
		self._simcond    = kwargs.get('simcond', "Sim09c")
		self._stripping  = kwargs.get('stripping', None)
		self._turbo      = kwargs.get('turbo', False)
		self._mudst      = kwargs.get('mudst', False)
		self._runnumber  = kwargs.get('runnumber', baserunnumber())
		self._decfiles   = kwargs.get('decfiles', 'v30r5')
		
		self._evttype = kwargs.get('evttype', None)	
		if self._evttype:
			self.__setoptfile()
		
		_basedir = os.getenv("SIMOUTPUT")
		if not _basedir:
			_basedir = os.getenv("HOME")+"/SimulationJobs"

		self._options["basedir"] = kwargs.get('basedir', _basedir)
		
		self._options["time"]    = kwargs.get('time', 16)
																			
		if IsSlurm():
			default_options    = DefaultSlurmOptions( )
			
			self._options["lsf"]      = False
			self._lsf                 = self._options["lsf"]
			self._options["slurm"]    = True	
			self._slurm               = self._options["slurm"]
			self._options["subtime"]  = kwargs.get('subtime', [0, 23])
			self._options["toeos"]    = False
						
			self._options["default_options"] = []
							
			def addvars(var):
				
				def make_get_set(var):
					def getter(self):
						return self._options[var]
					def setter(self, value):
						if isinstance(value, (int, float) ):
							self._options[var] = int( value )
							if var in self._options["default_options"]:
								self._options["default_options"].remove(var)
						else:
							raise TypeError(var + " must be a int!")
					return getter, setter
				
				get_set = make_get_set(var)
				self.__add_var(var, get_set)
			
			self._options["nsimjobs"]     = kwargs.get('nsimjobs', None)
			if not self._options["nsimjobs"]:
				self._options["nsimjobs"]             = default_options['nsimjobs']
				self._options["default_options"]     += ["nsimjobs"]
				
			addvars("nsimjobs")
													
			self._options["nsimuserjobs"] = kwargs.get('nsimuserjobs', None)
			if not self._options["nsimuserjobs"]:
				self._options["nsimuserjobs"]         = default_options['nsimuserjobs']
				self._options["default_options"]     += ["nsimuserjobs"]
				
			addvars("nsimuserjobs")
								
			self._options["nuserjobs"]    = kwargs.get('nuserjobs', None)
			if not self._options["nuserjobs"]:
				self._options["nuserjobs"]            = default_options['nuserjobs']
				self._options["default_options"]     += ["nuserjobs"]
				
			addvars("nuserjobs")
								
			self._options["npendingjobs"]  = kwargs.get('npendingjobs', None)
			if not self._options["npendingjobs"]:
				self._options["npendingjobs"]         = default_options['npendingjobs']
				self._options["default_options"]     += ["npendingjobs"]
				
			addvars("npendingjobs")
								
			self._options["nfreenodes"]    = kwargs.get('nfreenodes', None)
			if not self._options["nfreenodes"]:
				self._options["nfreenodes"]           = default_options['nfreenodes']
				self._options["default_options"]     += ["nfreenodes"]
				
			addvars("nfreenodes")
			
			self._options["nodestoexclude"] = kwargs.get('nodestoexclude', None)
			if not self._options["nodestoexclude"]:
				self._options["nodestoexclude"]       = default_options['nodestoexclude']
				self._options["default_options"]     += ["nodestoexclude"]
				
			addvars("nodestoexclude")
								
			self._options["cpu"]  = kwargs.get('cpu', None)
			if not self._options["cpu"]:
				self._options["cpu"]                  = default_options['cpu']
				self._options["default_options"]     += ["cpu"]
				
			addvars("npendingjobs")
								
		elif IsLSF():
			default_options    = DefaultLSFOptions()
			self._options["default_options"] = []
			
			if os.getenv("EOS_SIMOUTPUT"):
				self._options["toeos"]    = kwargs.get('toeos', True)
			else:
				self._options["toeos"]    = kwargs.get('toeos', False)
			
			if self._options["toeos"]:				
				self._options["eosdir"]  = kwargs.get('_eosdir', os.getenv("EOS_SIMOUTPUT"))
				
			self._options["lsf"]      = True
			self._lsf                 = self._options["lsf"]
			self._options["slurm"]    = False	
			self._slurm               = self._options["slurm"]
			
			self._options["cpu"]  = kwargs.get('cpu', None)
			if not self._options["cpu"]:
				self._options["cpu"]                  = default_options['cpu']
				self._options["default_options"]     += ["cpu"]
				
		self._screensessions = []
		self._inscreen       = False
											
	@property
	def nevents( self):
		return self._nevents
		
	@nevents.setter
	def nevents( self, value):
		if isinstance(value, (int, float) ):
			self._nevents = int( value )
		else:
			raise TypeError("nevents must be a int!")
				
	@property
	def neventsjob( self):
		return self._neventsjob
		
	@neventsjob.setter
	def neventsjob( self, value):
		if isinstance(value, (int, float) ):
			self._neventsjob = int( value )
		else:
			raise TypeError("nevents must be a int!")
		
	@property
	def nsubjobs( self):
		return self._nsubjobs
		
	@property
	def evttype( self):
		return self._evttype
		
	@evttype.setter
	def evttype( self, value ):
		self._evttype = value		
		self.__setoptfile()
		
	@property	
	def simcond( self):
		return self._simcond
		
	@simcond.setter	
	def simcond( self, value):
		if not isinstance(value, str):
			raise TypeError("simcond must be a str!")
		if not value in ["Sim09b", "Sim09c"]:
			raise ValueError("simcond must be Sim09b or Sim09c!")
		self._simcond = value
		
	@property	
	def stripping( self):
		return self._stripping
		
	@stripping.setter	
	def stripping( self, value):
		if not isinstance(value, str):
			raise TypeError("simcond must be a str!")
		if not value in ["21", "24", "28", "24r1", "24r1p1", "28r1", "28r1p1"]:
			raise ValueError("stripping must be '21, '24', '28', '24r1', '24r1p1', '28r1', or '28r1p1'!")
		self._simcond = value
		
	@property	
	def year( self):
		return self._year
		
	@year.setter
	def year( self, value):
		if not isinstance(value, int):
			raise TypeError("nevents must be a int!")
		if not value in [2011,2012,2015,2016,2017]:
			raise ValueError("year must be 2011, 2012, 2015, 2016 or 2017!")
		self._year = value
					
	@property	
	def options( self):
		return self._options
		
	@property	
	def proddir( self):
		return self._proddir
		
	@proddir.setter	
	def proddir( self, directory):
		if not os.path.isdir(directory):
			os.system("mkdir -p {0}".format(directory))
		self._proddir = directory
		
	@property	
	def destdir( self):
		return self._destdir
		
	@property	
	def optfile( self):
		return self._optfile
		
	@property	
	def turbo( self):
		return self._turbo
		
	@turbo.setter	
	def turbo( self, value):
		if isinstance(value, bool):
			self._turbo = value
		else:
			raise TypeError("turbo must be set to True/False!")
	
	@property	
	def mudst( self):
		return self._mudst
		
	@mudst.setter	
	def mudst( self, value):
		if isinstance(value, bool):
			self._mudst = value
		else:
			raise TypeError("mudst must be set to True/False!")
						
	def subjobs( self ):			
		return self._subjobs.values()
		
	def screensessions( self, i = None ):
		
		if not i:
			return self._screensessions
		else:
			if len(self._screensessions) < 1:
				raise NotImplementedError("No screen session attached to this simulation job.")
			elif i > len(self._screensessions):
				raise IndexError()
			elif ScreenExist(self._screensessions[i]["name"]):
				OpenScreenSession(self._screensessions[i]["name"])
			else:
				print("This screen does not exist!")
				KillScreenSession(self._screensessions[i]["name"])
				self._screensessions.remove(self._screensessions[i])
				
	def __removescreens( self ):
		for sc in self._screensessions:
			KillScreenSession(sc["name"])	
		self._screensessions = []
			
	def __getitem__(self, job_number):
		if not isinstance(job_number, int):
			raise TypeError("Job number must be a 'int'. Got a '{0}' instead!".format(job_number.__class__.__name__))
		return self._subjobs[str(job_number)]
			
	def __runnumber( self, job_number = None ):
		if job_number != None and not isinstance(job_number, int):
			raise TypeError("Job number must be a 'int'. Got a '{0}' instead!".format(job_number.__class__.__name__))
		
		if job_number == None:
			return self._runnumber
		else:
			return self._runnumber + job_number
		
	@property
	def status( self):
		nrunning   = 0
		ncompleted = 0 
		nfailed    = 0
		nsubmitted = 0
		
		for j in self.subjobs():
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
				
		if nsubmitted == 0:
			_status = "new"	
		elif nsubmitted < self.nsubjobs and nsubmitted > 0:
			_status = "submitting"
		elif nsubmitted == self.nsubjobs and nrunning == 0 and nfailed == 0 and ncompleted == 0:
			_status = "submitted"
		elif nsubmitted == self.nsubjobs and nrunning > 0:
			_status = "running"
		elif nsubmitted == self.nsubjobs and nrunning == 0 and ncompleted == self.nsubjobs and nfailed == 0:
			_status = "completed"
		elif nsubmitted == self.nsubjobs and nrunning == 0 and ncompleted < self.nsubjobs and nfailed > 0:
			_status = "failed"
			
		if _status != "submitting" or _status != "new":
			self.__removescreens()
			
		return _status
																		
	def prepare( self, job_number = None, **kwargs ):
		
		if len(self._subjobs) < 1:
				
			if not self._evttype:
				raise NotImplementedError('Evttype not defined!')
				
			if not self._nevents:
				raise NotImplementedError('nevents not defined!')
				
			if not self._neventsjob:
				raise NotImplementedError('neventsjob not defined!')
				
			if not self._year:
				raise NotImplementedError('year not defined!')
				
			if not self._simcond:
				raise NotImplementedError('simcond not defined!')
				
			self.__checksiminputs()
			
			#Number of jobs
			self._nsubjobs = int( self._nevents/ self._neventsjob )
			
			if  self._nsubjobs  == 0:
				warnings.warn( red(" WARNING: no jobs are being sent (make sure that neventsjob is smaller than nevents)! "), stacklevel = 2 )
			
			if not isinstance(self._polarity, list) or len(self._polarity) < self.nsubjobs:
				
				if not self._polarity:
					polarity = ["MagUp" for i in range(0,int(self.nsubjobs / 2))]
					polarity += ["MagDown" for i in range(int(self.nsubjobs / 2), self.nsubjobs)]
					shuffle(polarity)
					self._polarity = polarity
				else:
					self._polarity = [self._polarity for i in range(0, self.nsubjobs)]
				
			subdir = "simProd_{0}_{1}".format( self._evttype, self._simcond)
			if self._turbo:
				subdir += "_Turbo"
			if self._mudst:
				subdir += "_muDST"
			
			self._options["subdir"] = subdir
				
			self._proddir  = "{0}/{1}".format( self.options["basedir"], self.options["subdir"])
			
			if self._options.get("toeos", False):						
				self._options["eosproddir"]  = "{0}/{1}".format( self.options["eosdir"], self.options["subdir"])
				
			self._destdir = "{0}/{1}/{2}/{3}".format( self.__destination(), self._evttype, self._year, self._simcond)
				
		self._store_job()
		
		infiles = kwargs.get('infiles', [])

		for n in range(self.nsubjobs):
			if job_number != None and job_number != n:
				continue
				
			if self._subjobs.get(str(n), None):
				continue
			
			polarity  = self._polarity[n]
			runnumber = self.__runnumber(n)
			self._subjobs[str(n)] = SimulationSubJob( parent=self, polarity=polarity, runnumber=runnumber, infiles=infiles, jobnumber=n )
			
		
	def cancelpreparation( self, job_number = None, **kwargs ):
		
		for n in range(self.nsubjobs):
			if job_number != None and job_number != n:
				continue
				
			if self._subjobs.get(str(n), None):
				del self._subjobs[str(n)]
						
	def __cansubmit( self):
		if self._slurm:
			#update default options
			default_options  = DefaultSlurmOptions( )
			for opt in self.options["default_options"]:
				self.options[opt] = default_options[opt]
			return SubCondition( self.options )
		else:
			return True
				
	def send( self, job_number = None ):
		
		if (self._slurm and self._inscreen) or self._lsf:		
			try:
				for n in range(self.nsubjobs):
					if job_number != None and job_number != n:
						continue
					
					SUBMIT = False
					while SUBMIT == False:
						SUBMIT = self.__cansubmit()
						if not SUBMIT:
							time.sleep( randint(0,30) * 60 )
											
					if self[n]._submitted:
						continue	
					self[n].send
					
			except TypeError as e:
				print(e.message)
				raise NotImplementedError("Job is not prepared!") 
				
		elif self._slurm and not self._inscreen:
			
			### prepare the job submission through a screen session!
			
			cmdpy = self.__screencommandfile()
			
			screename = cmdpy.replace(".py","")
			screename = screename.replace(os.path.dirname(screename)+"/","")
			
			_id = SendInScreen( screename, cmdpy)
			
			print(red("Job submission is done in a screen session!"))
			
			self._screensessions.append({"name":screename, "id":_id})

	def __checksiminputs( self ):
		
		def StrippingVersion( *args ):
			args = list(args)
			with warnings.catch_warnings():
				warnings.simplefilter("always")	
				if self._stripping == None:
					self._stripping = args[0]
					if len(args) > 1:
						warnings.warn( red("Default stripping version {0} used. {1} versions are available.".format( 
										self._stripping, 
									   	args)), 
									   	stacklevel = 2)
				elif self._stripping not in args:
					raise NotImplementedError( "Stripping version {0} is not available for {1} {2}! Only {3}!".format( 
									   	self._stripping, 
									   	self._year, 
									   	self._simcond, 
									   	args) )	
						
		if self._simcond == "Sim09b" and ( self._year == 2011 or self._year == 2017 ):
			raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
										self._year, 
										self._simcond) )
			
		elif self._simcond == "Sim09c" and self._year == 2017:
			raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
										self._year, 
										self._simcond) )
		
		if self._year == 2012:
			if self._simcond == "Sim09b":
				StrippingVersion("21")
			elif self._simcond == "Sim09c":
				StrippingVersion("21")
			
		elif self._year == 2015:
			if self._simcond == "Sim09b":
				StrippingVersion("24")
			if self._simcond == "Sim09c":
				StrippingVersion("24r1", "24r1p1")
			
		elif self._year == 2016:
			if self._simcond == "Sim09b":
				StrippingVersion("28")
			if self._simcond == "Sim09c":
				StrippingVersion("28r1", "28r1p1")	
								
		if self._mudst and ( self._year == 2012 or self._year == 2011 ):
			raise NotImplementedError( "No micro DST output for {0}!".format(self._year) )
				
		if self._turbo and ( self._year == 2012 or self._year == 2011 ):
			raise NotImplementedError( "Turbo is not implemented for {0}!".format(self._year) )
			
	def __setoptfile( self ):
		moddir = os.getenv("SIMPRODPATH")
		self._optfile = "{0}/EvtTypes/{1}/{1}.py".format( moddir, self._evttype )
	
		if not os.path.isfile( self._optfile ):
			GetEvtType.get( evttype = self._evttype, decfiles = self._decfiles )
			
	def __add_var(self, var, get_set):
		setattr(SimulationJob, var, property(*get_set))
		self.__dict__[var] = getattr(SimulationJob, var)
		
	def _store_job(self, storesubjobs = False):
		simprod = os.getenv("SIMPRODPATH")+"/simprod"
		jobsdir = "{0}/._simjobs_".format(simprod)
		
		if not os.path.isdir(jobsdir):
			os.system("mkdir -p {0}".format(jobsdir))
				
		jobfile = "{0}/{1}_{2}_{3}_{4}_{5}.json".format(
					jobsdir,
					self.evttype,
					self.year,
					self.nevents,
					self.neventsjob,
					self._runnumber,
					)
					
		outdict = {"evttype":         self.evttype,
				   "year"   :	      self.year,
				   "nevents":         self.nevents,
				   "neventsjob":      self.neventsjob,
				   "runnumber":       self._runnumber,
				   "simcond":         self.simcond,
				   "stripping":       self.stripping,
				   "mudst":           self.mudst,
				   "turbo":           self.turbo,
				   "basedir":         self.options["basedir"],
				   "nsubjobs":        self.nsubjobs,
				   "proddir" :        self.proddir,
				   "destdir":         self.destdir,
				   "subdir":          self.options["subdir"],
				   "slurm":           self.options["slurm"],
				   "lsf":             self.options["lsf"],
				   "toeos":		      self.options["toeos"],
				   "_screensessions": self._screensessions,
				   "jobs":        {}
				   } 
				
		if self._options["toeos"]:
			outdict["eosdir"] = self.options["eosdir"]
			outdict["eosproddir"] = self.options["eosproddir"]
			
		outdict["default_options"] = self.options["default_options"]
		outdict["cpu"]             = self.options["cpu"]
			
		if self._options["slurm"]:	
			outdict["nsimjobs"]     = self.options["nsimjobs"]
			outdict["nsimuserjobs"] = self.options["nsimuserjobs"]
			outdict["nuserjobs"]    = self.options["nuserjobs"]
			outdict["npendingjobs"] = self.options["npendingjobs"]
			outdict["nfreenodes"]   = self.options["nfreenodes"]
					
		jsondict = json.dumps(outdict)
		f = open(jobfile, "w")
		f.write(jsondict)
		f.close()
		
		if storesubjobs:
			for i in range(self.nsubjobs):
				job = self[i]
				job._store_subjob()
				
		self._options["jobfile"] = jobfile
		
	def remove( self ):
				
		if self.status == "running":
			raise NotImplementedError("Cannot remove running jobs!")

		if os.path.isfile(self.options["jobfile"]):
			os.remove(self.options["jobfile"])
		
		for k in self._subjobs.keys():
			job = self[int(k)]
			job.kill()
			
		self.__removescreens()
													
	@classmethod
	def from_file(cls, file, inscreen = False):
		data = json.load(open(file))
		simjob = cls( 
					evttype    = data["evttype"],
					year       = data["year"],
					nevents    = data["nevents"],
					neventsjob = data["neventsjob"],
					runnumber  = data["runnumber"],
					simcond    = data["simcond"],
					stripping  = data["stripping"],
					mudst      = data["mudst"],
					turbo      = data["turbo"],	
					basedir    = data["basedir"]
					)						
			
		simjob._nsubjobs = data["nsubjobs"]
		simjob._proddir  = data["proddir"]
		simjob._destdir  = data["destdir"]
		simjob._options["subdir"] = data["subdir"]
		simjob._options["slurm"]  = data["slurm"]
		simjob._options["lsf"]    = data["lsf"]
		simjob._options["toeos"]  = data["toeos"]
		simjob._options["jobfile"] = file
		
		if simjob._options["toeos"]:
			simjob._options["eosdir"]     = data["eosdir"]
			simjob._options["eosproddir"] = data["eosproddir"]
			
		simjob._options["cpu"]             = data["cpu"]
		simjob._options["default_options"] = data["default_options"]
		
		if simjob._options["slurm"]:
			simjob._options["nsimjobs"]     = data["nsimjobs"]
			simjob._options["nsimuserjobs"] = data["nsimuserjobs"]
			simjob._options["nuserjobs"]    = data["nuserjobs"]
			simjob._options["npendingjobs"] = data["npendingjobs"]
			simjob._options["nfreenodes"]   = data["nfreenodes"]
			
		if inscreen:
			simjob._inscreen = True
		else:
			simjob._screensessions = data["_screensessions"]

		### prepare like 
				
		jobs = data["jobs"]
				
		for n in jobs.keys():
			simjob._subjobs[n] = SimulationSubJob.from_dict(
										parent = simjob, 
										jobnumber = n, 
										dict = jobs[n])													
		return simjob
		
	def __str__(self):
		
		if len(self._subjobs) > 0:
			toprint  = "evttype: {0}; year: {1}; #events {2}; stripping {3}; simcond {4}; {5} jobs\n".format( 
						self.evttype,
						self.year,
						self.nevents,
						self.stripping,
						self.simcond,
						self.nsubjobs )
			
			h_job        = "    #job "
			h_jobID      = "    job ID "
			h_status     = "       status "
			h_runnumber  = "      runnumber "
			h_polarity   = "   polarity "
			h_nevents    = "  #events "
			
			header = "{0}|{1}|{2}|{3}|{4}|{5}|\n".format( 
						h_job,
						h_jobID, 
						h_status, 
						h_runnumber, 
						h_polarity, 
						h_nevents)
						
			line = "-"*(len(header) - 2) + "\n"	
			toprint += line
			toprint += header
			
			toprint += line
			
			for i in range(self.nsubjobs):
				
				job = self[i]
								
				status    = job.status
				jobID     = job.jobid
				runnumber = job.runnumber
				polarity  = job.polarity
				nevents   = self.neventsjob
				
				if status == "submitted":
					color = cyan
				elif status == "new":
					color = cdefault
				elif status == "running":
					color = green
				elif status == "completed":
					color = blue
				elif status == "failed":
					color = red
						
				p_job       = "{n:{fill}{al}{w}} ".format(w=(len(h_job)-1), al='>', fill='', n=i)
				
				p_jobID     = "{n:{fill}{al}{w}} ".format(w=(len(h_jobID)-1), al='>', fill='', n=jobID)
				
				p_status    = "{n:{fill}{al}{w}} ".format(w=(len(h_status)-1), al='>', fill='', n=status)
				
				p_runnumber = "{n:{fill}{al}{w}} ".format(w=(len(h_runnumber)-1), al='>', fill='', n=runnumber)
				
				p_polarity  = "{n:{fill}{al}{w}} ".format(w=(len(h_polarity)-1), al='>', fill='', n=polarity)
				
				p_nevents   = "{n:{fill}{al}{w}} ".format(w=(len(h_nevents)-1), al='>', fill='', n=nevents)
										
				toprint += color("{0}|{1}|{2}|{3}|{4}|{5}|\n".format( 
							p_job, 
							p_jobID,
							p_status, 
							p_runnumber, 
							p_polarity, 
							p_nevents))						
		else:
			toprint = self.__repr__()
		
		return toprint
		
	def _repr_pretty_(self, p, cycle):
		if cycle:
			p.text('simulation job...')
			return
		p.text(self.__str__())
		
	def __destination(self):

		if self.options["toeos"]:
			return self.options["eosdir"]
		else:
			return self.options["basedir"]
			
	def __screencommandfile(self):
		
		simprod = os.getenv("SIMPRODPATH")+"/simprod"
		jobsdir = "{0}/._simjobs_".format(simprod)
		
		screenfile = "{0}/{1}_{2}_{3}_{4}_{5}_{6}.py".format(
					jobsdir,
					self.evttype,
					self.year,
					self.nevents,
					self.neventsjob,
					self._runnumber,
					len(self._screensessions)
					)
		
		f = open(screenfile, "w")
		f.write("#!/usr/bin/python\n\n")
		
		f.write("import os\n")
		f.write("os.environ['SIMPRODPATH'] = '{0}'\n".format(os.getenv("SIMPRODPATH")))
		f.write("os.environ['SIMOUTPUT'] = '{0}'\n".format(os.getenv("SIMOUTPUT")))
		f.write("from simprod import *\n\n")
		
		f.write("job = SimulationJob().from_file('{0}', inscreen = {1})\n".format(
										self._options["jobfile"],
										True,
										))
		f.write("job.send()\n\n")
		f.write("os.remove(__file__)\n\n")
		f.close()
		
		return screenfile
		
					
class SimulationSubJob(object):
	"""
	Simulation subjob.
	"""
	
	def __init__(self, parent, polarity, runnumber, jobnumber, **kwargs):
		self._parent       = parent
		self._polarity     = polarity
		self._runnumber    = runnumber
		self._jobnumber    = jobnumber
		self._jobid        = None
		self._send_options = self._parent.options.copy()
		self._status       = "new"
						
		self._infiles = kwargs.get('infiles', [])
		if not isinstance(self._infiles, list) and " " in self._infiles:
			self._infiles = self._infiles.split(" ")
		elif not isinstance(self._infiles, list):
			self._infiles = [self._infiles]
		
		self._jobname = "{0}_{1}_{2}evts_s{3}_{4}".format( 
							self._parent.year, 
							self._polarity, 
							self._parent.neventsjob, 
							self._parent.stripping, 
							self._runnumber )
							
		_subdir = "{0}_{1}_{2}evts_s{3}_{4}".format( 
							self._parent.year, 
							self._polarity, 
							self._parent.neventsjob, 
							self._parent.stripping, 
							self._runnumber)
							
		self._ext = "dst"	
		if self._parent.mudst:
			self._ext = "mdst"
								
		self._jobdir = "{0}/{1}".format(
						self._parent.proddir,
						_subdir)		
			
		self._prodfile = "{0}/{1}_events.{2}".format( 
						self._jobdir,
						self._parent.neventsjob, 
						self._ext )
							
		if self._send_options["toeos"]:
			self._eosjobdir = "{0}/{1}".format(
							self._send_options["eosproddir"],
							_subdir)	
			
			self._eosprodfile = "{0}/{1}_events.{2}".format( 
							self._eosjobdir,
							self._parent.neventsjob, 
							self._ext )
											
		self._destfile = "{0}/{1}/{2}evts_s{3}_{4}.{5}".format( 
								self._parent.destdir, 
								self._polarity, 
								self._parent.neventsjob, 
								self._parent.stripping, 
								self.runnumber, 
								self._ext )
		
		self._send_options["jobname"] = self._jobname
		self._send_options["infiles"] = self._infiles
		self._send_options["command"] = self._command()
		
		self._submitted = False
		self._running   = False
		self._finished  = False
		self._completed = False
		self._failed    = False
		
		if not kwargs.get("from_dict", False):
			self._store_subjob()
		
	@property
	def jobdir( self):
		return self._jobdir
				
	@property
	def prodfile( self):
		return self._prodfile
		
	@property
	def destfile( self):
		return self._destfile
				
	@property	
	def send( self):
		if not self._submitted or self._failed:
			send_options = self._send_options
			self._jobid = submit( **send_options )
			self._submitted = True
			self._running   = False
			self._finished  = False
			self._completed = False
			self._failed    = False
			self._store_subjob()
						
			time.sleep(0.07)
			print( blue( "{0}/{1} jobs submitted!".format( int(self._jobnumber) + 1, self._parent.nsubjobs ) ) )
			time.sleep(0.07)
			
			
	@property
	def jobid( self):
		return self._jobid
		
	@property
	def polarity( self):
		return self._polarity
		
	@property
	def runnumber( self):
		return self._runnumber
					
	@property
	def status( self):
		
		_previous = self._status
		
		if not self._finished and self._submitted:
			self.__updatestatus()
		if not self._submitted:
			self._status = "new"
		elif self._submitted and not self._running and not self._finished:
			self._status = "submitted"
		elif self._submitted and self._running and not self._finished:
			self._status = "running"
		elif self._submitted and not self._running and self._finished:
			if self._completed:
				self._status = "completed"
				if not self.output == self.destfile:
					self.__move_jobs()
			elif self._failed:
				self._status = "failed"
				self.__empty_proddir(keep_log = True)
				
		if _previous != self._status:
			print("status of job (evttype {0}, year {1}, run number {2}) changed from '{3}' to '{4}'.".format(
							self._parent.evttype,
							self._parent.year,
							self._runnumber, 
							_previous, 
							self._status)
							)
			self._store_subjob()
				
		return self._status
				
	@property
	def step( self):
		raise NotImplementedError
		
	@property
	def application( self):
		raise NotImplementedError
				
	@property
	def out( self):
		raise NotImplementedError
		
	@property
	def err( self):
		raise NotImplementedError
		
	@property
	def output( self):
		if os.path.isfile( self._prodfile):
			return self._prodfile
		elif os.path.isfile( self._destfile):
			return self._destfile
		elif self._send_options["toeos"] and os.path.isfile(self._eosprodfile):
			return self._eosprodfile		
		else:
			return ""
			
	def _command( self ):
		doprod  = DoProd( self._parent.simcond, self._parent.year)
		
		command  = doprod
		command += ' {0}'.format( self._parent.optfile)
		command += ' {0}'.format( self._parent.neventsjob)
		command += ' {0}'.format( self._polarity)
		command += ' {0}'.format( self._runnumber)
		command += ' {0}'.format( self._parent.turbo)
		command += ' {0}'.format( self._parent.mudst)
		command += ' {0}'.format( self._parent.stripping)
			
		return command
					
	def __updatestatus( self):
		if self._send_options["slurm"]:
			status = GetSlurmStatus( self.jobid )								
		elif self._send_options["lsf"]:
			status = GetLSFStatus( self.jobid )
						
		if status == "running":
			self._running   = True
			
		elif status == "completed" or status == "canceled" or status == "failed" or status == "notfound":
			self._running  = False
			self._finished = True
						
			if self.output != "" and os.path.isfile( self.output ):							
				if os.path.isfile( self.output ) and os.path.getsize( self.output ) > 900000:
					self._completed = True
				elif os.path.isfile( self.output ) and os.path.getsize( self.output ) < 900000:
					self._failed = True	
			elif self.output == "":
				self._failed = True
				
	def kill( self ):
		if self._running and not self._finished:
			if self._send_options["slurm"]:
				KillSlurm( self.jobid )
			elif self._send_options["lsf"]:
				KillLSF( self.jobid )
				
			self._failed = True
			self._running = False
			self._completed = False
			self._finished  = True
			self._store_subjob()
			self.__empty_proddir()
			
	def __empty_proddir( self, keep_log = False ):
		if os.path.isdir(self._jobdir):
			if keep_log:
				files = glob.glob(self._jobdir + "/*")
				for f in files:
					if "out" in f:
						continue
					elif "err" in f:
						continue
					else:
						os.remove(f) 
			else:
				os.system("rm -rf {0}".format(self._jobdir))
		if self._send_options["toeos"] and os.path.isdir(self._eosjobdir):
			os.system("rm -rf {0}".format(self._eosjobdir))
			
	def __move_jobs( self ):
		
		if self._send_options["toeos"]:
			dst_prodfile = self._eosprodfile
			mover = EosMove
		else:
			dst_prodfile = self._prodfile
			mover = Move
			
		xml_prodfile = os.path.dirname(dst_prodfile) + "/GeneratorLog.xml"	
		dst_destfile = self.destfile
		xml_destfile = os.path.dirname(self.destfile) + "/xml/{0}.xml".format(self.runnumber)

		print("Moving job (evttype {0}, year {1}, run number {2}) to final destination!".format(self._parent.evttype, self._parent.year, self._runnumber))
		mover( dst_prodfile, dst_destfile )
		mover( xml_prodfile, xml_destfile )
		
		self.__empty_proddir()
		
	def _store_subjob(self):
		
		_jobfile = self._parent.options["jobfile"]
		_dict = json.load(open(_jobfile))	
				
		_subjob = {
			       "runnumber":   self.runnumber,
			       "polarity":    self.polarity,
			       "_jobid":      self.jobid,
				   "_prodfile":   self.prodfile,
			       "_jobdir":     self.jobdir,
				   "_destfile":   self.destfile,
				   "_submitted":  self._submitted,
				   "_running":    self._running,
				   "_finished":   self._finished,
				   "_completed":  self._completed,
				   "_failed":     self._failed,
				   "_status":     self._status,
					  }
		if self._send_options["toeos"]:
			_subjob["_eosprodfile"] = self._eosprodfile
			_subjob["_eosjobdir"]   = self._eosjobdir
			
		_dict["jobs"][str(self._jobnumber)] = _subjob
						
		jsondict = json.dumps(_dict)
		f = open(_jobfile, "w")
		f.write(jsondict)
		f.close()
		
	@classmethod
	def from_dict(cls, parent, jobnumber, dict):
		
		simsubjob = cls( parent    = parent, 
						 polarity  = dict["polarity"],
		                 runnumber = dict["runnumber"],
						 jobnumber = jobnumber,
						 from_dict = True
						)
						
		simsubjob._jobid     = dict["_jobid"]
		simsubjob._profile   = dict["_prodfile"]
		simsubjob._jobdir    = dict["_jobdir"]
		simsubjob._destfile  = dict["_destfile"]
		simsubjob._submitted = dict["_submitted"]
		simsubjob._running   = dict["_running"]
		simsubjob._finished  = dict["_finished"]
		simsubjob._completed = dict["_completed"]
		simsubjob._failed    = dict["_failed"]
		simsubjob._status    = dict["_status"]
				
		if simsubjob._send_options["toeos"]:
			simsubjob._eosprodfile = dict["_eosprodfile"]
			simsubjob._eosjobdir   = dict["_eosjobdir"]
		
		return simsubjob
		
	
	
		
		
		
				

