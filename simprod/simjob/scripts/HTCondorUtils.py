#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch

from subprocess import Popen, PIPE
from datetime import datetime
import os
from .utils import *
import sys
from .submit import SendCommand
import htcondor
import getpass
import datetime
from .Status import Status
import re
import shutil
import subprocess as sub

DEBUG = 0

def DefaultHTCondorOptions():
	
	options = {}		
	options["jobflavour"] = 'workday'
		
	return options
	
def run(command):
	process = Popen(command, stdout=PIPE, shell=True)
	while True:
		line = process.stdout.readline().rstrip()
		if not line:
			break
		yield line
	
	
class Scheduler():
	
	def __init__(self):
		self._schedd = htcondor.Schedd()
		self.query = None
	
	def getquery(self):
		user = getpass.getuser()
		try:
			query = self._schedd.query('User=="{0}@cern.ch"'.format(user), ["ClusterID", "JobStatus", "ProcID"])
			self.query = QueryResult(query)
			return True
		except (RuntimeError, IOError):
			print(red("Failed to query job status. Thank you HTCondor ... Try later!"))
			return False
			
	def getcluster(self, ClusterID):
		if self.query is None:
			if not self.getquery():
				return BadQuery()
		else:
			if not self.query.isvalid:
				if not self.getquery():
					return BadQuery()
				
		if self.query is None:
			return None
		else:
			ret = []
			for q in self.query:
				if q["ClusterID"] == ClusterID:
					ret.append(q)
			return QueryResult(ret)
			
	def act(self, *args, **kwargs):
		self._schedd.act(*args, **kwargs)
			
	def renew(self):
		self._schedd = htcondor.Schedd()
		
class BadQuery(object):
	
	def __init__(self, *args, **kwargs):
		pass
			
class QueryResult(object):
	
	def __init__(self, query):
		
		self.query = query
		self.creation_time = datetime.datetime.now()
		self._cache = {}

	@property
	def isvalid(self):
		now = datetime.datetime.now()
		elapsedTime = now - self.creation_time
		minutes = divmod(elapsedTime.total_seconds(), 60)[0]
		if minutes > 3:
			return False
		else:
			return True
		
	def __iter__(self):
		for q in self.query:
			yield q
			
	def getProcID(self, ID):
		ret = None
		
		if ID in self._cache.keys():
			ret = self._cache[ID]
		else:
			querys = list(self.query)
			for q in querys:
				if ID == q["ProcID"]:
					ret = q
					self._cache[ID] = q
					self.query.remove(q)
		return ret

class DeliveryClerk(object):
	
	def __init__(self, **kwargs):
		
		default_options = DefaultHTCondorOptions()
		self.default_options = default_options
		self._schedd = kwargs.get("scheduler")
		self._query = None
		
		self.defaults = []
		options = {}
				
		options["subtime"] = kwargs.get("subtime", [0, 23])
		
		options["jobflavour"] = kwargs.get("jobflavour", default_options['jobflavour'])
		self.defaults += ["jobflavour"]
		
		self.options = options
		
		self.addvar("jobflavour", allowed_values = ["espresso", "microcentury", "longlunch", "workday",
													"tomorrow", "testmatch", "nextweek"])
		
		
	def outdict(self):
		return {"options": self.options}
		
		
	@classmethod
	def from_dict(cls, dict, **kwargs):
		deliveryclerk = cls(**dict["options"])	
		deliveryclerk._schedd = kwargs.get("scheduler", None)	
		return deliveryclerk
			
						
	def send_job(self, job, *args, **kwargs):
		
		logdir = job.options["logdestdir"]
		
		if not os.path.exists(job.proddir):
			os.makedirs(job.proddir) 
		if not os.path.exists(job.destdir):
			os.makedirs(job.destdir) 
		if not os.path.exists(logdir):
			os.makedirs(logdir) 
			
		subfile = "{logdir}/run.sub".format(logdir=logdir)
		runfile = subfile.replace(".sub", ".sh")
		
		if os.path.isfile(subfile):
			os.remove(subfile)
		if os.path.isfile(runfile):
			os.remove(runfile)
			
		doprod = "{0}/{1}".format(logdir, os.path.basename(job.doprod))
		if not os.path.isfile(doprod):
			shutil.copyfile(job.doprod, doprod)
			sub.call(['chmod', '775', doprod])
			
		create_runfile(runfile, doprod)
		 
		condor = open(subfile, "w")
		condor.write("executable = {runfile}\n".format(runfile=runfile))
		condor.write("output = $(subjob_log_dir)/out\n")
		condor.write("error = $(subjob_log_dir)/err\n")
		condor.write("log = {logdir}/$(ClusterId).log\n".format(logdir=logdir))
		condor.write('+JobFlavour = "{jobflavour}"\n\n'.format(jobflavour=self.options["jobflavour"]))
		
		submitted_jobs = []
		
		ext = "mdst" if job.mudst else "dst"
		nevts = job.neventsjob
		
		for n in job.range_subjobs:	
			sj = job[n]
			if not sj._status.submitted:
				sjlogdir = "{logdir}/{sjname}".format(logdir=logdir, sjname=sj.jobname)
				if os.path.isdir(sjlogdir):
					shutil.rmtree(sjlogdir, ignore_errors = True)
				os.makedirs(sjlogdir)
				if os.path.isdir(sj.jobdir):
					shutil.rmtree(sj.jobdir, ignore_errors = True)
				os.makedirs(sj.jobdir)
				
				if sj.infiles:
					condor.write("transfer_input_files = {0}\n".format(",".join(sj.infiles))
					
				condor.write("subjob_log_dir={sjlogdir}\n".format(sjlogdir=sjlogdir))
				args = " ".join(str(a) for a in sj.command()["args"])
				condor.write("arguments = {args}\n".format(args=args))
				totransfer = 'transfer_output_remaps = "{nevts}_events.{ext}={prodfile} '.format(nevts=nevts, ext=ext, prodfile=sj.prodfile)
				totransfer += ' ; GeneratorLog.xml={dir}/GeneratorLog.xml"\n'.format(dir=sj.jobdir)
				condor.write(totransfer)
				condor.write("queue\n\n")	
				submitted_jobs.append(sj)
		condor.close()
		
		command = "condor_submit {subfile}".format(subfile=subfile)
				
		print(blue("Submitting jobs: ...."))

		out = SendCommand(command)
		try:
			ClusterID = int(float(out.split("\n")[1].split(" ")[-1]))
			print(blue(out.split("\n")[1]))
		except IndexError:
			print(red("job {0} submission failed, try later!".format(job.jobnumber)))
			ClusterID = None
			
		if ClusterID is not None:
			for n, sj in enumerate(submitted_jobs):
				sj.jobid = "{0}.{1}".format(ClusterID, n)
				sj._status = Status("submitted", sj.output)
			
												
	def send_subjob(self, subjob):
		if not subjob._status.submitted or subjob._status.failed:
			if subjob._status.failed:
				subjob.reset()
				
			job = subjob.parent
				
			logdir = job.options["logdestdir"]
			
			if not os.path.exists(job.proddir):
				os.makedirs(job.proddir) 
			if not os.path.exists(job.destdir):
				os.makedirs(job.destdir) 
			if not os.path.exists(logdir):
				os.makedirs(logdir) 
				
			subfile = "{logdir}/run_sj_{sjnum}.sub".format(logdir=logdir, sjnum=subjob.subjobnumber)
			runfile = subfile.replace(".sub", ".sh")
			
			if os.path.isfile(subfile):
				os.remove(subfile)
			if os.path.isfile(runfile):
				os.remove(runfile)
				
			doprod = "{0}/{1}".format(logdir, os.path.basename(job.doprod))
			if not os.path.isfile(doprod):
				shutil.copyfile(job.doprod, doprod)
				sub.call(['chmod', '775', doprod])
				
			create_runfile(runfile, doprod)
			
			condor = open(subfile, "w")
			condor.write("executable = {runfile}\n".format(runfile=runfile))
			condor.write("output = $(subjob_log_dir)/out\n")
			condor.write("error = $(subjob_log_dir)/err\n")
			condor.write("log = {logdir}/$(ClusterId).log\n".format(logdir=logdir))
			condor.write('+JobFlavour = "{jobflavour}"\n\n'.format(jobflavour=self.options["jobflavour"]))
			
			submitted_jobs = []
			
			ext = "mdst" if job.mudst else "dst"
			nevts = job.neventsjob
			
			sjlogdir = "{logdir}/{sjname}".format(logdir=logdir, sjname=subjob.jobname)
			if os.path.isdir(sjlogdir):
				shutil.rmtree(sjlogdir, ignore_errors = True)
			os.makedirs(sjlogdir)
			if os.path.isdir(subjob.jobdir):
				shutil.rmtree(subjob.jobdir, ignore_errors = True)
			os.makedirs(subjob.jobdir)
			
			if subjob.infiles:
				condor.write("transfer_input_files = {0}\n".format(",".join(subjob.infiles))
				
			condor.write("subjob_log_dir={sjlogdir}\n".format(sjlogdir=sjlogdir))
			args = " ".join(str(a) for a in subjob.command()["args"])
			condor.write("arguments = {args}\n".format(args=args))
			totransfer = 'transfer_output_remaps = "{nevts}_events.{ext}={prodfile} '.format(nevts=nevts, ext=ext, prodfile=subjob.prodfile)
			totransfer += ' ; GeneratorLog.xml={dir}/GeneratorLog.xml"\n'.format(dir=subjob.jobdir)
			condor.write(totransfer)
			condor.write("queue\n\n")	
			condor.close()
			
			command = "condor_submit {subfile}".format(subfile=subfile)

			print(blue("Submitting jobs ...."))
			
			out = SendCommand(command)
			try:
				ClusterID = int(float(out.split("\n")[1].split(" ")[-1]))
				print(blue(out.split("\n")[1]))
			except IndexError:
				print(red("job {0} submission failed, try later!".format(job.jobnumber)))
				ClusterID = None
			
			if ClusterID is not None:	
				subjob.jobid = "{0}.{1}".format(ClusterID, n)
				subjob._status = Status("submitted", subjob.output)
			
			
	def getstatus(self, ID):
		
		if not isinstance(ID, str):
			ID = str(ID)
			
		ClusterID = int(ID.split(".")[0])
		ProcID = int(ID.split(".")[1])
		
		if DEBUG > 0:
			print("in HTCondorUtils.DeliveryClerk.getstatus")
			print("ClusterID: ", ClusterID)
			print("ProcID: ", ProcID)
			
		if DEBUG > 0:	
			print(self._query)
		
		if self._query is None:
			self._query = self._schedd.getcluster(ClusterID)
		if DEBUG > 0:	
			print(self._query)
			
		if self._query is None:
			return "new"
		elif isinstance(self._query, BadQuery):
			return "error"
		else:	
			if not self._query.isvalid:
				self._query = self._schedd.getcluster(ClusterID)
				
			if isinstance(self._query, BadQuery):
				return "error"
					
			queryjob = self._query.getProcID(ProcID)
			if queryjob is None:
				return "notfound"
			else:
				status = queryjob["JobStatus"]
				
				if status in [0, 3, 5, 6]:
					return "failed"
				elif status == 1:
					return "submitted"
				elif status == 2:
					return "running"
				elif status == 4:
					return "completed"
				else:
					return "notfound"
				
	
	def get_update_subjobs(self, job):
		return None
		
		
	def clear(self, job):
		pass
	
	
	def kill(self, **kwargs):
		job = kwargs["job"]

		cluster_ids = []
		for sj in job:
			ID = sj.jobid
			if ID is None:
				continue
			if not isinstance(ID, str):
				ID = str(ID)
			ClusterID = int(ID.split(".")[0])
			
			if ClusterID not in cluster_ids:
				cluster_ids.append(ClusterID)
					
		for cid in cluster_ids:
			try:
				self._schedd.act(htcondor.JobAction.Remove, 'ClusterId=={0}'.format(cid))
			except RuntimeError:
				kill = Popen(['condor_rm', str(cid)], stdout=PIPE, stderr=PIPE)
				out, err = kill.communicate()
				
		return False

			
	def killsubjob(self, ID):
		try:
			if not isinstance(ID, str):
				ID = str(ID)
			ClusterID = int(ID.split(".")[0])
			ProcID = int(ID.split(".")[1])
			self._schedd.act(htcondor.JobAction.Remove, 'ClusterId=={0} && ProcID=={1}'.format(ClusterID, ProcID))
		except RuntimeError:
			kill = Popen(['condor_rm', str(ID)], stdout=PIPE, stderr=PIPE)
			out, err = kill.communicate()	
			
				
	def addvar(self, var, allowed_values=[]):
		
		def make_get_set(var):
			def getter(self):
				return self.options[var]
			def setter(self, value):
				if type(value) != type(self.default_options[var]):
					msg = "A {} is required!".format(type(self.default_options[var]))
					raise TypeError(msg)
					
				if len(allowed_values) > 1 and value not in allowed_values:
					raise ValueError("Allowed values for {0} are {1}".format(var, allowed_values))
					
				self.options[var] = value
				if var in self.defaults:
					self.defaults.remove(var)
				
			return getter, setter
		
		get_set = make_get_set(var)
		
		setattr(DeliveryClerk, var, property(*get_set))
		self.__dict__[var] = getattr(DeliveryClerk, var)
	
		
def create_runfile(namefile, doprod):
	
	user = getpass.getuser()
	
	runscript = open(namefile, "w")
	runscript.write("#!/bin/bash\n")
	runscript.write("shopt -s expand_aliases\n")
	runscript.write('export PATH="/bin:/usr/local/bin:/usr/bin:$PATH"\n')
	runscript.write('export HOME="{}"\n'.format(os.environ["HOME"]))
	runscript.write('export USER="{user}"\n'.format(user=user))
	runscript.write('source /cvmfs/lhcb.cern.ch/group_login.sh\n')
	runscript.write('{doprod} $1 $2 $3 $4 $5 $6 $7 $8\n'.format(doprod=doprod))
	runscript.close()
	
	sub.call(['chmod', '775', namefile])



	
	
