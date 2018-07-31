#!/usr/bin/python
# -*- coding: utf-8 -*-

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: simulation job class

from .scripts import *
import os
import time
from random import randint, shuffle
from .setup import DoProd
import warnings
import glob
import json
import bisect
from tqdm import tqdm
from colorama import Fore

class JobCollection(object):
	"""
	Simulation job collection.
	"""
	
	def __init__(self, **kwargs):

		self._jobs     = {}
		self._jsondict = {}
		self._keys     = []	
		self._slurm    = IsSlurm()
		
		simprod = os.getenv("SIMPRODPATH")+"/simprod"		
		self._jobsdir   = "{0}/._simjobs_".format(simprod)
		self._collection_file = "{0}/collection.json".format(self._jobsdir)

		if os.path.isfile( self._collection_file ):
			with open(self._collection_file, 'r') as f:
				_collectedjobs = json.load(f)
			self._jsondict = _collectedjobs
			
			if len(_collectedjobs) > 0:	
						
				print(red("\nLoading Jobs:"))
				t = tqdm(total=len(_collectedjobs))
				
				for cj in _collectedjobs.keys():
					bisect.insort(self._keys, int(cj))
					fields = ["file", "status", "evttype", "year", "nevents", "nsubjobs"]
					
					if all(i in _collectedjobs[cj] for i in fields):
						
						_file = _collectedjobs[cj]["file"]
						if not os.path.isfile(_file):
							t.update(1)
							continue
						
						if _collectedjobs[cj]["status"] == "completed":
							print("HEHO")
							print(cj)
							job = None
						else:
							job = SimulationJob().from_file(_file, cj)
							
						self._jobs[str(cj)] = job
						self._jsondict[str(cj)] = _collectedjobs[cj] 
						
					else:
						if "file" in _collectedjobs[cj]:
							_file = _collectedjobs[cj]["file"]
						else:
							_file = _collectedjobs[cj]

						if not os.path.isfile(_file):
							t.update(1)
							continue
							
						self._add_job(_file, cj)
							
					t.update(1)
					
				t.close()
		self.__update(in_init = True)
							
	def __str__(self):
		self.__update()
		
		toprint = []		
		toprint.append("{0} jobs".format(len(self._jobs)))
		
		h_job     = "    #job "
		h_status  = "       status "
		h_evttype = "       evttype "
		h_year    = "   year "
		h_nevents = "  #events "
		h_subjobs = "  #subjobs "
		
		header = "|".join([h_job, h_status, h_evttype, h_year, h_nevents, h_subjobs]) + "|"
		line   = "".join(["-" for i in xrange(len(header) - 2)])
				
		toprint.append(line)
		toprint.append(header)
		toprint.append(line)
		
		for k in self._keys:
			
			job     = self._jobs[str(k)]
			
			if job is not None:
				status  = job.status
				evttype = job.evttype
				year    = job.year
				nevents = job.nevents
				subjobs = job.nsubjobs
				self._jsondict[str(k)]["status"]   = status
				self._jsondict[str(k)]["evttype"]  = evttype
				self._jsondict[str(k)]["year"]     = year
				self._jsondict[str(k)]["nevents"]  = nevents
				self._jsondict[str(k)]["nsubjobs"] = subjobs
			
			else:
				status  = self._jsondict[str(k)]["status"]
				evttype = self._jsondict[str(k)]["evttype"]
				year    = self._jsondict[str(k)]["year"]
				nevents = self._jsondict[str(k)]["nevents"]
				subjobs = self._jsondict[str(k)]["nsubjobs"]
			
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
								
			p_job     = "{n:{fill}{al}{w}} ".format(w=(len(h_job)-1), al='>', fill='', n=k)
						
			p_status  = "{n:{fill}{al}{w}} ".format(w=(len(h_status)-1), al='>', fill='', n=status)
			
			p_evttype = "{n:{fill}{al}{w}} ".format(w=(len(h_evttype)-1), al='>', fill='', n=evttype)
			
			p_year    = "{n:{fill}{al}{w}} ".format(w=(len(h_year)-1), al='>', fill='', n=year)
			
			p_nevents = "{n:{fill}{al}{w}} ".format(w=(len(h_nevents)-1), al='>', fill='', n=nevents)
			
			p_subjobs = "{n:{fill}{al}{w}} ".format(w=(len(h_subjobs)-1), al='>', fill='', n=subjobs)
			
			linejob = "|".join([p_job, p_status, p_evttype, p_year, p_nevents, p_subjobs]) + "|"
						
			toprint.append(color(linejob))
			
		toprint = "\n".join(toprint)
						
		return toprint
		
	def _repr_pretty_(self, p, cycle):
		if cycle:
			p.text('job collection...')
			return
		p.text(self.__str__())
		
	def __getitem__(self, i):
		if i != None and not isinstance(i, int):
			raise TypeError("Job number must be a 'int'. Got a '{0}' instead!".format(i.__class__.__name__))
		if i not in self._keys and i > max(self._keys):
			self.__update()
		if i not in self._keys:
			raise ValueError("job {0} not found!".format(i))
		else:
			if self._jobs[str(i)] is None:
				print(green("\nLoading Job {0}:".format(i)))
				_file = self._jsondict[str(i)]["file"]
				job = SimulationJob().from_file(_file, i)
				self._jobs[str(i)] = job 
			else:
				job = self._jobs[str(i)]
			
			return job
			
	def __iter__(self):
		for k in self._keys:
			yield self._jobs[str(k)]		
	
	def __len__(self):
		return len(self._keys)
			
	def select(self, status):
		return [self[k] for k in self._keys if self[k].status == status]
		
	def __update(self, in_init = False):		
		jsonfiles = glob.iglob("{0}/*/job.json".format(self._jobsdir))
		
		for k, item in self._jsondict.iteritems():
			_file = item["file"]
			if not os.path.isfile(_file):
				try:
					self._keys.remove(int(k))
				except ValueError:
					continue
			elif not in_init and self._slurm:
				jobstatus = item["status"]
				if jobstatus == "new" or jobstatus == "submitting":
					self._jobs[str(k)]._update_subjobs(jobstatus)
																	
		self._jsondict = { k : v for k,v in self._jsondict.iteritems() if int(k) in self._keys }
		self._jobs     = { k : v for k,v in self._jobs.iteritems() if int(k) in self._keys }
		
		files = [i["file"] for i in self._jsondict.values()]
		
		for js in jsonfiles:			
			if js not in files:
				if len(self._jsondict) < 1:
					index = 0
				else:
					index = self._keys[-1] + 1
				print(green("\nLoading new Job {0}:".format(index)))	
				self._add_job(js, index)
				
				bisect.insort(self._keys, index)
				
		self._store_collection()
		
	def _add_job(self, jsonfile, index):
		
		job = SimulationJob().from_file(jsonfile, index)
		self._jobs[str(index)] = job 
		
		_dict = {}
		_dict["file"] = js
		_dict["status"] = job.last_status
		_dict["evttype"]  = job.evttype
		_dict["year"]     = job.year
		_dict["nevents"]  = job.nevents
		_dict["nsubjobs"] = job.nsubjobs
		self._jsondict[str(index)] = _dict
		
	def _store_collection(self):
				
		if not os.path.isdir(self._jobsdir):
			os.makedirs(self._jobsdir)
								
		jsondict = json.dumps(self._jsondict)
		f = open(self._collection_file, "w")
		f.write(jsondict)
		f.close()
			
				
class SimulationJob(object):
	"""
	Simulation job
	"""
	
	def __init__(self, **kwargs):			
		self._subjobs = {}
		self._subjobs_dict = {}
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
		self._decfiles   = kwargs.get('decfiles', 'v30r16')
		self._inscreen   = kwargs.get('inscreen', False)
		self._keeplogs   = kwargs.get('keeplogs', True)
		self._keepxmls   = kwargs.get('keepxmls', True)
		self._redecay    = kwargs.get('redecay', False)
		self._jobnumber  = None
		self._status     = "new"
		
		self._evttype = kwargs.get('evttype', None)	
		if self._evttype:
			self.__setoptfile()
		
		_basedir = os.getenv("SIMOUTPUT")
		if not _basedir:
			_basedir = os.getenv("HOME")+"/SimulationJobs"

		self._options["basedir"] = kwargs.get('basedir', _basedir)
		
		self._options["time"]    = kwargs.get('time', None)
		if not self._options["time"]:
			self._options["time"] = 10 
			
		def addvars(var, _type = (int, float), allowed_values = []):
			
			def make_get_set(var):
				def getter(self):
					return self._options[var]
				def setter(self, value):
					if isinstance(value, _type ):
						if len(allowed_values) > 1 and not value in allowed_values:
							raise ValueError("Allowed values for {0} are {1}".format(var, allowed_values))
						self._options[var] = value	
						if var in self._options["default_options"]:
							del self._options["default_options"][var]
					else:
						raise TypeError(var + " must be a {0}!".format(_type))
				return getter, setter
			
			get_set = make_get_set(var)
			self.__add_var(var, get_set)
																			
		if IsSlurm():
			default_options    = DefaultSlurmOptions( )
			
			self._options["lsf"]      = False
			self._lsf                 = self._options["lsf"]
			self._options["slurm"]    = True	
			self._slurm               = self._options["slurm"]
			self._options["subtime"]  = kwargs.get('subtime', [0, 23])
			self._options["loginprod"] = True
						
			self._options["default_options"] = []
						
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
								
			self._options["cpumemory"]      = kwargs.get('cpumemory', None)
			if not self._options["cpumemory"]:
				self._options["cpumemory"]            = default_options['cpumemory']
				self._options["default_options"]     += ["cpumemory"]
				
			addvars("cpumemory")
				
			self._options["totmemory"]      = kwargs.get('totmemory', None)
			if not self._options["totmemory"]:
				self._options["totmemory"]           = default_options['totmemory']
				self._options["default_options"]     += ["totmemory"]
								
			addvars("totmemory")
								
		elif IsLSF():
			default_options    = DefaultLSFOptions()
			self._options["default_options"] = []
			
			if os.getenv("LOG_SIMOUTPUT"):
				self._options["loginprod"] = kwargs.get('loginprod', False)
			else:
				self._options["loginprod"] = kwargs.get('loginprod', True)
				
			if not self._options["loginprod"]:
				self._options["logdir"]    = kwargs.get('logdir', os.getenv("LOG_SIMOUTPUT"))
				
			self._options["lsf"]    = True
			self._lsf               = self._options["lsf"]
			self._options["slurm"]  = False	
			self._slurm             = self._options["slurm"]
			
			self._options["cpumemory"]     = kwargs.get('cpumemory', None)
			if not self._options["cpumemory"]:
				self._options["cpumemory"]        = default_options['cpumemory']
				self._options["default_options"] += ["cpumemory"]
				
			addvars("cpumemory")
			
			self._options["queue"] = kwargs.get('queue', '1nd')
			addvars("queue", _type = (str), allowed_values = ["8nm","1nh","8nh","1nd","2nd","1nw","2nw"])
				
		self._screensessions = []
											
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
		self.__updateoptions()
		return self._options
		
	@property	
	def proddir( self):
		return self._proddir
		
	@proddir.setter	
	def proddir( self, directory):
		if not os.path.isdir(directory):
			os.makedirs(directory)
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
			
	@property
	def keeplogs( self):
		return self._keeplogs
		
	@keeplogs.setter	
	def keeplogs( self, value):
		if isinstance(value, bool):
			self._keeplogs = value
		else:
			raise TypeError("keeplogs must be set to True/False!")
			
	@property
	def keepxmls( self):
		return self._keepxmls
		
	@keepxmls.setter	
	def keepxmls( self, value):
		if isinstance(value, bool):
			self._keepxmls = value
		else:
			raise TypeError("keepxmls must be set to True/False!")
			
	@property
	def redecay( self):
		return self._redecay
		
	@redecay.setter	
	def redecay( self, value):
		if isinstance(value, bool):
			self._redecay = value
		else:
			raise TypeError("redecay must be set to True/False!")
	
	@property					
	def subjobs( self ):	
		return self._subjobs.itervalues()
		
	def __runnumber( self, job_number = None ):
		if job_number != None and not isinstance(job_number, int):
			raise TypeError("Job number must be a 'int'. Got a '{0}' instead!".format(job_number.__class__.__name__))
		
		if job_number == None:
			return self._runnumber
		else:
			return self._runnumber + job_number
		
	def prepare( self, **kwargs ):
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
				
				self._neventsjob = int(self._nevents / 2)
				self._nevents    = self._neventsjob * 2
				self._nsubjobs   = 2
			
			if not isinstance(self._polarity, list):
				
				if not self._polarity:
					polarity = ["MagUp" for i in xrange(0,int(self.nsubjobs / 2))]
					polarity += ["MagDown" for i in xrange(int(self.nsubjobs / 2), self.nsubjobs)]
					self._polarity = shuffle(polarity)
				else:
					self._polarity = [self._polarity for i in xrange(0, self.nsubjobs)]
					
				
			subdir = "simProd_{0}_{1}".format( self._evttype, self._simcond)
			if self._turbo:
				subdir += "_Turbo"
			if self._mudst:
				subdir += "_muDST"
			if self._redecay: 
				subdir += "_ReDecay"
			
			self._options["subdir"] = subdir
				
			self._proddir  = "{0}/{1}".format( self.options["basedir"], self.options["subdir"])
						
			if not self.options.get("loginprod", True):						
					self._options["logdestdir"]  = "{0}/{1}".format( self.options["logdir"], self.options["subdir"])
				
			self._destdir = "{0}/{1}/{2}/{3}".format( self.__destination(), self._evttype, self._year, self._simcond)
			
			if self._redecay:
				self._destdir += "_ReDecay"
				
		self._store_job()
		
		infiles = kwargs.get('infiles', [])

		for n in xrange(self.nsubjobs):				
			if self._subjobs.get(str(n), None):
				continue
				
			self._preparesubjobs(n, infiles = infiles, keeplog = self._keeplogs, keepxml = self._keepxmls)
						
	def _preparesubjobs( self, sjn, **kwargs ):
						
		if self._polarity:	
			polarity  = self._polarity[sjn]
		else:
			if sjn <= int(self.nsubjobs/2):
				polarity = "MagUp"
			else:
				polarity = "MagDown"
				
		_dict = {}
		
		status    = job.status
		jobID     = job.jobid
		runnumber = job.runnumber
		polarity  = job.polarity
		nevents   = self.neventsjob
		
		_dict["jobid"] = None
		_dict["status"] = "new"
		_dict["polarity"] = polarity
			
		runnumber = self.__runnumber(sjn)
		self._subjobs[str(sjn)] = SimulationSubJob( parent=self, polarity=polarity, runnumber=runnumber, subjobnumber=sjn, **kwargs )	
		
		self._subjobs_dict[str(sjn)] = _dict
						
	def send( self, job_number = None ):
				
		if (self._slurm and self._inscreen) or self._lsf:		
			try:
				for n in xrange(self.nsubjobs):
					if job_number != None and job_number != n:
						continue
					
					SUBMIT = False
					while SUBMIT == False:
						SUBMIT = self._cansubmit()
						if not SUBMIT:
							time.sleep( randint(0,30) * 60 )
											
					if self[n]._submitted:
						continue	
					self[n].send()
					
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
			
		self._store_job(storesubjobs = True)	
		
					
	def cancelpreparation( self, **kwargs ):	
		for n in xrange(self.nsubjobs):				
			if self._subjobs.get(str(n), None):
				del self._subjobs[str(n)]
			
	def __updateoptions(self):
		if self._slurm:
			#update default options
			default_options  = DefaultSlurmOptions( )
			for opt in self._options["default_options"]:
				self._options[opt] = default_options[opt]
					
	def _cansubmit( self):
		self.__updateoptions()
		if self._slurm:
			return SubCondition( self._options )
		else:
			return True
			
	def remove( self ):
		
		if self._jobnumber:
			info_msg = "INFO\tremoving job {0}".format(self._jobnumber)
		else:
			info_msg = "INFO\tremoving job"
		print(info_msg)
				
		for sj in self.subjobs:
			if sj.status == "running":
				sj.kill()

		if os.path.isdir(self.options["job_storage_dir"]):
			silentrm( self.options["job_storage_dir"] )
			
		self.__removescreens()
		
	def resend( self):		
		failedsubjobs = self.select("failed")
				
		if len(failedsubjobs) > 0:
			
			for sj in failedsubjobs:
				sj.reset()
				
			if (self._slurm and self._inscreen) or self._lsf:
				for sj in failedsubjobs:
					
					SUBMIT = False
					while SUBMIT == False:
						SUBMIT = self._cansubmit()
						if not SUBMIT:
							time.sleep( randint(0,30) * 60 )
											
					if sj._submitted:
						continue	
					sj.send()
					
			elif self._slurm and not self._inscreen:
				
				subjobnumbers = [sj._subjobnumber for sj in failedsubjobs]
				
				cmdpy = self.__screencommandfile( subjobnumbers )
				
				screename = cmdpy.replace(".py","")
				screename = screename.replace(os.path.dirname(screename)+"/","")
				
				_id = SendInScreen( screename, cmdpy)
				
				print(red("Job submission is done in a screen session!"))
				
				self._screensessions.append({"name":screename, "id":_id})
				
			self._store_job(storesubjobs = True)
		else:
			print("INFO\tNothing to re-send!")
	
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
				del self._screensessions[self._screensessions[i]]
				
	def __removescreens( self ):
		for sc in self._screensessions:
			KillScreenSession(sc["name"])	
		self._screensessions = []
			
	def __getitem__(self, job_number):
		if not isinstance(job_number, int):
			raise TypeError("Job number must be a 'int'. Got a '{0}' instead!".format(job_number.__class__.__name__))
		try:
			self._subjobs[str(job_number)]
		except KeyError:
			print("WARNING\tsubjob {0}.{1} has been lost!".format(self._jobnumber, job_number))
			self._preparesubjobs( job_number )
			
		if self._subjobs[str(job_number)] is None:
			
			job_storage_dir = self._options["job_storage_dir"]
				
			subjobfile = "{0}/subjob_{1}.json".format(job_storage_dir, job_number)
			
			subjob = SimulationSubJob.from_file( parent = self, 
												 subjobnumber = str(job_number), 
											     file   = subjobfile)
											
			self._subjobs[str(job_number)] = subjob

		return self._subjobs[str(job_number)]
			
	def select(self, status):
		return [self[n] for n in xrange(self.nsubjobs) if self[n].status == status]
		
	@property
	def last_status( self):	
		return self._status
					
	@property
	def status( self):	
		if not(self._status == "completed"):
							
			nrunning   = 0
			ncompleted = 0 
			nfailed    = 0
			nsubmitted = 0
			
			for n in xrange(self._nsubjobs):
				
				if self._subjobs[str(n)] is None:
					status = self._subjobs_dict[str(n)]["status"]
					
				else:
					status = self[n].status
							
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
			elif nsubmitted == self.nsubjobs and nrunning == 0 and nfailed == 0 and ncompleted < self.nsubjobs:
				_status = "submitted"
			elif nsubmitted == self.nsubjobs and nrunning > 0:
				_status = "running"
			elif nsubmitted == self.nsubjobs and nrunning == 0 and ncompleted == self.nsubjobs and nfailed == 0:
				_status = "completed"
			elif nsubmitted == self.nsubjobs and nrunning == 0 and ncompleted < self.nsubjobs and nfailed > 0:
				_status = "failed"
				
			if _status != "submitting" and _status != "new":
				self.__removescreens()
				
			if _status != self._status:
				info_msg = "INFO\tstatus of job {0} changed from '{1}' to '{2}'".format( 
																					self._jobnumber,
																					self._status,
																					_status)													
				print(info_msg)
				self._status = _status
				self._store_job(True)
				
			self._status = _status
			
		return self._status
																		
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
						
		if self._simcond == "Sim09b" and self._year in [2011, 2017]:
			raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
										self._year, 
										self._simcond) )
			
		elif self._simcond == "Sim09c" and self._year == 2017:
			raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
										self._year, 
										self._simcond) )
			
		elif self._simcond == "Sim09d" and self._year in [2011, 2012, 2015, 2016, 2017]:
			raise NotImplementedError( "{0} setup is not (yet) implemented for {1}!".format(
										self._year, 
										self._simcond) )							
		
										
		if self._year == 2011:
			if self._simcond == "Sim09c":
				StrippingVersion("21r1")
		
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
			getevttype( evttype = self._evttype, decfiles = self._decfiles )
			
	def __add_var(self, var, get_set):
		setattr(SimulationJob, var, property(*get_set))
		self.__dict__[var] = getattr(SimulationJob, var)
		
	def _store_job(self, storesubjobs = False):
		simprod = os.getenv("SIMPRODPATH")+"/simprod"
		_dir_ = "{0}/._simjobs_".format(simprod)
		
		if not os.path.isdir(_dir_):
			os.makedirs(_dir_)
		
		job_storage_dir = "{0}/{1}_{2}_{3}_{4}_{5}".format(
					_dir_,
					self.evttype,
					self.year,
					self.nevents,
					self.neventsjob,
					self._runnumber,
					)
					
		if not os.path.isdir(job_storage_dir):
			os.makedirs(job_storage_dir)
			
		job_jsonfile = "{0}/job.json".format(job_storage_dir)
					
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
				   "loginprod":       self.options["loginprod"],    
				   "_screensessions": self._screensessions,
				   "status":          self.status,
				   "keeplogs":        self._keeplogs,
				   "keepxmls":        self._keepxmls,
				   "redecay":         self._redecay,
				   "subjobs_dict":    self._subjobs_dict
				   } 
				
		if not self.options["loginprod"]:
			outdict["logdir"]     = self.options["logdir"]
			outdict["logdestdir"] = self.options["logdestdir"]
				
		outdict["default_options"] = self.options["default_options"]
		outdict["cpumemory"]       = self.options["cpumemory"]
			
		if self._options["slurm"]:	
			outdict["nsimjobs"]     = self.options["nsimjobs"]
			outdict["nsimuserjobs"] = self.options["nsimuserjobs"]
			outdict["nuserjobs"]    = self.options["nuserjobs"]
			outdict["npendingjobs"] = self.options["npendingjobs"]
			outdict["nfreenodes"]   = self.options["nfreenodes"]
			outdict["totmemory"]    = self.options["totmemory"]
					
		jsondict = json.dumps(outdict)
		
		with open(job_jsonfile, 'w') as f:
			f.write(jsondict)
		
		self._options["job_storage_dir"] = job_storage_dir
		self._options["job_jsonfile"]  = job_jsonfile
		
		if storesubjobs:
			for i in xrange(self.nsubjobs):
				job = self[i]
				if job:
					job._store_subjob()
																	
	@classmethod
	def from_file(cls, file, jobnumber = None, inscreen = False):
		
		with open(file, 'r') as f:
			data = json.load(f)
			
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
		
		simjob._jobnumber = jobnumber	
		simjob._nsubjobs = data["nsubjobs"]
		simjob._proddir  = data["proddir"]
		simjob._destdir  = data["destdir"]
		simjob._options["subdir"] = data["subdir"]
		simjob._options["slurm"]  = data["slurm"]
		simjob._options["lsf"]    = data["lsf"]
		simjob._options["loginprod"] = data["loginprod"]
		simjob._options["job_jsonfile"] = file
		simjob._options["job_storage_dir"] = data.get("job_storage_dir", os.path.dirname(file))
		simjob._screensessions = data["_screensessions"]
		simjob._status = data.get("status", "new")
		simjob._keeplogs = data.get("keeplogs", True)
		simjob._keepxmls = data.get("keepxmls", True)
		simjob._redecay  = data.get("redecay", False)
		simjob._subjobs_dict  = data.get("subjobs_dict", {})
				
		if not simjob._options["loginprod"]:
			simjob._options["logdir"]     = data["logdir"]
			simjob._options["logdestdir"] = data["logdestdir"]
			
		simjob._options["cpumemory"]       = data.get("cpumemory", None)
		if not simjob._options["cpumemory"]:
			simjob._options["cpumemory"]   = data.get("cpu", None)
		
		simjob._options["default_options"] = data["default_options"]
		
		if simjob._options["slurm"]:
			simjob._options["nsimjobs"]     = data["nsimjobs"]
			simjob._options["nsimuserjobs"] = data["nsimuserjobs"]
			simjob._options["nuserjobs"]    = data["nuserjobs"]
			simjob._options["npendingjobs"] = data["npendingjobs"]
			simjob._options["nfreenodes"]   = data["nfreenodes"]
			simjob._options["totmemory"]    = data.get("totmemory", None)
		if inscreen:
			simjob._inscreen = True
		
		t = tqdm(total=simjob._nsubjobs, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET), desc = cyan("\tLoading subjobs"))

		if "jobs" in data:
			for n, subjob in data["jobs"].items():				
				simjob._subjobs[str(n)] = SimulationSubJob.from_file(
											parent = simjob, 
											subjobnumber = str(n), 
											file   = subjob)
				t.update(1)
											
			simjob._store_job(True)
			
			
		else:
			to_store = False
					
			for n in range(simjob._nsubjobs):
				job_storage_dir = simjob._options["job_storage_dir"]
					
				subjobfile = "{0}/subjob_{1}.json".format(job_storage_dir, n)
				
				
				subjob = SimulationSubJob.from_file( parent = simjob, 
													 subjobnumber = str(n), 
												     file   = subjobfile)
														
				if not str(n) in simjob._subjobs_dict:								
					to_store = True
														
					simjob._subjobs[str(n)] = subjob
					_dict = {}					
					_dict["jobid"]    = subjob.jobid
					_dict["status"]   = subjob.last_status
					_dict["polarity"] = subjob.polarity	
					simjob._subjobs_dict[str(n)] = _dict
					
				if simjob._subjobs_dict[str(n)]["status"] == "completed":
					simjob._subjobs[str(n)] = None	
				else:
					simjob._subjobs[str(n)] = subjob
									
				t.update(1)
										
			if to_store:
				simjob._store_job(False)
																					
		t.close()
												
		return simjob	
		
	def _update_subjobs(self, status="new"):	
		job_storage_dir = self.options["job_storage_dir"]
					
		for n in xrange(self.nsubjobs):
			sj = self[n]
			if sj.status == status:		
				
				subjobfile = "{0}/subjob_{1}.json".format(job_storage_dir, n)
				
				with open(subjobfile, 'r') as f:
					subjob = json.load(f)
							
				if subjob["_submitted"]:
					self._subjobs[str(n)] = SimulationSubJob.from_file( parent = self, 
																        	subjobnumber = str(n), 
																        	file = subjobfile)
																
																																								
	def __str__(self):
		
		if len(self._subjobs) > 0:
			
			toprint = []
			
			toprint.append("evttype: {0}; year: {1}; #events {2}; stripping {3}; simcond {4}; {5} jobs".format( 
						self.evttype,
						self.year,
						self.nevents,
						self.stripping,
						self.simcond,
						self.nsubjobs ))
			
			h_job        = "    #job "
			h_jobID      = "    job ID "
			h_status     = "       status "
			h_runnumber  = "      runnumber "
			h_polarity   = "   polarity "
			h_nevents    = "  #events "
			
			header = [h_job, h_jobID, h_status, h_runnumber, h_polarity, h_nevents]
			header = "|".join(header) + "|"	
			line   = "".join(["-" for i in xrange(len(header) - 2)])
					
			toprint.append(line)
			toprint.append(header)
			toprint.append(line)

			for n in xrange(self.nsubjobs):
				
				if self._subjobs[str(n)] is None:
					job = self._subjobs_dict[str(n)]
					status    = job["status"] 
					jobID     = job["jobid"]
					runnumber = self.__runnumber(n)
					polarity  = job["polarity"]
				else:				
					job = self[n]				
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
						
				p_job       = "{n:{fill}{al}{w}} ".format(w=(len(h_job)-1), al='>', fill='', n=n)
				
				p_jobID     = "{n:{fill}{al}{w}} ".format(w=(len(h_jobID)-1), al='>', fill='', n=jobID)
				
				p_status    = "{n:{fill}{al}{w}} ".format(w=(len(h_status)-1), al='>', fill='', n=status)
				
				p_runnumber = "{n:{fill}{al}{w}} ".format(w=(len(h_runnumber)-1), al='>', fill='', n=runnumber)
				
				p_polarity  = "{n:{fill}{al}{w}} ".format(w=(len(h_polarity)-1), al='>', fill='', n=polarity)
				
				p_nevents   = "{n:{fill}{al}{w}} ".format(w=(len(h_nevents)-1), al='>', fill='', n=nevents)
				
				linejob = "|".join([p_job, p_jobID, p_status, p_runnumber, p_polarity, p_nevents]) + "|"
				
				toprint.append(color(linejob))
				
			toprint = "\n".join(toprint)
									
		else:
			toprint = self.__repr__()
		
		return toprint
		
	def _repr_pretty_(self, p, cycle):
		if cycle:
			p.text('simulation job...')
			return
		p.text(self.__str__())
		
	def __destination(self):

		return self.options["basedir"]
			
	def __screencommandfile(self, subjobnumbers = None):
		
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
		f.write("import time\n")
		f.write("os.environ['SIMPRODPATH'] = '{0}'\n".format(os.getenv("SIMPRODPATH")))
		f.write("os.environ['SIMOUTPUT'] = '{0}'\n".format(os.getenv("SIMOUTPUT")))
					
		f.write("from simprod import *\n\n")
		
		f.write("time.sleep(1.5)\n\n")
		
		f.write("job = SimulationJob().from_file('{0}', inscreen = {1}, jobnumber = {2})\n".format(
										self._options["job_jsonfile"],
										True,
										self._jobnumber
										))
		if subjobnumbers:
			for j in subjobnumbers:
				f.write("job.send({0})\n".format(j))
		else:
			f.write("job.send()\n")
		f.write("\n")
		f.write("os.remove(__file__)\n\n")
		f.close()
		
		return screenfile
							
class SimulationSubJob(object):
	"""
	Simulation subjob.
	"""
	
	def __init__(self, parent, polarity, runnumber, subjobnumber, **kwargs):
		self._parent       = parent
		self._polarity     = polarity
		self._runnumber    = runnumber
		self._subjobnumber = subjobnumber
		self._jobid        = None
		self._send_options = self._parent.options.copy()
		self._status       = "new"
		self._keeplog      = kwargs.get('keeplog', True)
		self._keepxml      = kwargs.get('keepxml', True)
						
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
														
		self._ext = "dst"	
		if self._parent.mudst:
			self._ext = "mdst"
								
		self._jobdir = "{0}/{1}".format(
						self._parent.proddir,
						self._jobname)		
			
		self._prodfile = "{0}/{1}_events.{2}".format( 
						self._jobdir,
						self._parent.neventsjob, 
						self._ext )
							
		if not self._send_options["loginprod"]:
			self._logjobdir = "{0}/{1}".format(
							self._send_options["logdestdir"],
							self._jobname)
			
														
		self._destfile = "{0}/{1}/{2}evts_s{3}_{4}.{5}".format( 
								self._parent.destdir, 
								self._polarity, 
								self._parent.neventsjob, 
								self._parent.stripping, 
								self.runnumber, 
								self._ext )
		
		self._send_options["jobname"] = self._jobname
		self._send_options["infiles"] = self._infiles
		self._send_options["command"] = self.__command()
		
		self._submitted = False
		self._running   = False
		self._finished  = False
		self._completed = False
		self._failed    = False
		
		if not kwargs.get("from_file", False):
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
				
	def send( self):
		
		SUBMIT = False
		while SUBMIT == False:
			SUBMIT = self._parent._cansubmit()
			if not SUBMIT:
				time.sleep( randint(0,20) * 60 )
		
		if not self._submitted or self._failed:
			if self._failed:
				self.reset()
			
			send_options = self._send_options
			self._jobid = submit( **send_options )
			
			if self._jobid:
				self._submitted = True
				self._running   = False
				self._finished  = False
				self._completed = False
				self._failed    = False
				self._store_subjob()
							
				time.sleep(0.07)
				print( blue( "{0}/{1} jobs submitted!".format( int(self._subjobnumber) + 1, self._parent.nsubjobs ) ) )
				time.sleep(0.07)				
			else:
				print( red( "job {0}/{1} submission failed, try later!".format( int(self._subjobnumber) + 1, self._parent.nsubjobs ) ) )
					
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
	def last_status( self):
		return self._status
					
	@property
	def status( self):
		
		_previous = self._status
		
		if not(_previous == "failed" or _previous == "completed"):
			
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
					if not self.output == self.destfile and not self.output == "":
						self.__move_jobs()
				elif self._failed:
					self._status = "failed"
					self.__empty_proddir(keep_log = True)
					
			if _previous != self._status:
				
				if self._parent._jobnumber:
					info_msg = "INFO\tstatus of subjob {0}.{1} changed from '{2}' to '{3}'".format( 
												self._parent._jobnumber,
											    self._subjobnumber,
												_previous,
												self._status)
				else:
					info_msg = "INFO\tstatus of job (evttype {0}, year {1}, run number {2}) changed from '{3}' to '{4}'.".format(
												self._parent.evttype,
												self._parent.year,
												self._runnumber, 
												_previous, 
												self._status)					
				print(info_msg)	
				self._store_subjob()
				
		return self._status
		
	@property
	def infiles( self):
		return self._send_options["infiles"]
		
	@infiles.setter
	def infiles( self, listfiles):
		if not isinstance(listfiles, list):
			raise ValueError("infiles shoud be a list!")
		self._send_options["infiles"] = listfiles
		self._infiles = listfiles
				
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
		else:
			return ""
			
	def reset( self):
		
		if self._status == "completed":
			self.kill()
			
		self.__empty_proddir()
		self._jobid     = None
		self._submitted = False
		self._running   = False
		self._finished  = False
		self._completed = False
		self._failed    = False
		self._status    = "new"
		self._store_subjob()
			
	def __command( self ):
		doprod  = DoProd( self._parent.simcond, self._parent.year)
		
		command  = doprod
		command += ' {0}'.format( self._parent.optfile)
		command += ' {0}'.format( self._parent.neventsjob)
		command += ' {0}'.format( self._polarity)
		command += ' {0}'.format( self._runnumber)
		command += ' {0}'.format( self._parent.turbo)
		command += ' {0}'.format( self._parent.mudst)
		command += ' {0}'.format( self._parent.stripping)
		command += ' {0}'.format( self._parent.redecay)
			
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
		
		if self._parent._jobnumber:
			info_msg = "INFO\tkilling subjob {0}.{1}".format( self._parent._jobnumber,
															  self._subjobnumber)
		else:
			info_msg = "INFO\tkilling subjob {0}".format(self._subjobnumber)
		
		print(info_msg)
		
		if self._submitted:
			if self._send_options["slurm"]:
				KillSlurm( self.jobid )
			elif self._send_options["lsf"]:
				KillLSF( self.jobid )
				
		self._failed = True
		self._running = False
		self._completed = False
		self._finished  = True
		self._status    = "failed"
		self._store_subjob()
		self.__empty_proddir()
			
	def __empty_proddir( self, keep_log = False ):
		if os.path.isdir(self._jobdir):
			if keep_log and self._send_options["loginprod"]:
				files = glob.iglob(self._jobdir + "/*")
				for f in files:
					if "out" in f:
						continue
					elif "err" in f:
						continue
					else:
						os.remove(f) 
			else:
				silentrm(self._jobdir)
				
		if not self._send_options["loginprod"] and not keep_log:
			if os.path.isdir(self._logjobdir):
				silentrm(self._logjobdir)
				
	def __move_jobs( self ):
		
		if not os.path.isdir(self._jobdir):
			warnings.warn( red(" WARNING: production folder has been removed, if the jobs is marked as failed the output has "
			+"been probably lost!"), stacklevel = 2 )
			
		else:
			dst_prodfile = self._prodfile

			if "eos" in dst_prodfile:
				mover = EosMove
			else:
				mover = Move
					
			xml_prodfile = os.path.dirname(dst_prodfile) + "/GeneratorLog.xml"	
			dst_destfile = self.destfile
			xml_destfile = os.path.dirname(self.destfile) + "/xml/{0}.xml".format(self.runnumber)
			
			
			if self._parent._jobnumber:
				info_msg = "INFO\tMoving subjob {0}.{1} to final destination!".format( self._parent._jobnumber,
																    self._subjobnumber)
			else:
				info_msg = "INFO\tMoving subjob (evttype {0}, year {1}, run number {2}) to final destination!".format(
											self._parent.evttype,
											self._parent.year,
											self._runnumber)
					
			print(info_msg)
			
			if os.path.isfile(dst_prodfile):
				mover( dst_prodfile, dst_destfile )
			else:
				warn_msg = red("WARNING\tdst output is not found. It has probably been moved or erased manually")
				print(warn_msg)
				
			if self._keepxml:		
				if os.path.isfile(xml_prodfile):
					mover( xml_prodfile, xml_destfile )
				else:
					warn_msg = red("WARNING\tGeneratorLog.xml is not found. It has probably been moved or erased manually")
					print(warn_msg)
				
			self.__empty_proddir( self._keeplog )
		
	def _store_subjob(self):
		
		job_storage_dir = self._parent.options["job_storage_dir"]
			
		subjobfile = "{0}/subjob_{1}.json".format(job_storage_dir, self._subjobnumber)
				
		outdict = {
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
				   "_infiles":    self._infiles,
				   "_keeplog":    self._keeplog,
				   "_keepxml":    self._keepxml,
				   }
					
		if not self._send_options["loginprod"]:
			outdict["_logjobdir"]   = self._logjobdir
						
		jsondict = json.dumps(outdict)
		
		with open(subjobfile, 'w') as f:
			f.write(jsondict)
		
	@classmethod
	def from_file(cls, parent, subjobnumber, file, tqdm = None):
		
		if isinstance(file, dict):
			data = file
		else:	
			with open(file, 'r') as f:
				data = json.load(f)
		
		simsubjob = cls( parent    = parent, 
						 polarity  = data["polarity"],
		                 runnumber = data["runnumber"],
						 subjobnumber = subjobnumber,
						 from_file = True
						)
						
		simsubjob._jobid     = data["_jobid"]
		simsubjob._profile   = data["_prodfile"]
		simsubjob._jobdir    = data["_jobdir"]
		simsubjob._destfile  = data["_destfile"]
		simsubjob._submitted = data["_submitted"]
		simsubjob._running   = data["_running"]
		simsubjob._finished  = data["_finished"]
		simsubjob._completed = data["_completed"]
		simsubjob._failed    = data["_failed"]
		simsubjob._status    = data["_status"]
		simsubjob._infiles   = data.get("_infiles",[])
		simsubjob._keeplog   = data.get("_keeplog", True)
		simsubjob._keepxml   = data.get("_keepxml", True)
		simsubjob._send_options["infiles"] = data.get("_infiles",[])
								
		if not simsubjob._send_options["loginprod"]:
			simsubjob._logjobdir = data["_logjobdir"]
		
		return simsubjob
		
	
	
		
		
		
				

