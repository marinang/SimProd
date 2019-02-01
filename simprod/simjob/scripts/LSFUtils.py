#!/usr/bin/python

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch

from subprocess import Popen, PIPE
from datetime import datetime
import os
from .utils import *
import sys
from .submit import main as submit
from .Status import Status

def Kill(ID):
	
	kill = Popen(['bkill',str(ID)], stdout=PIPE, stderr=PIPE)
	out, err = kill.communicate()	
		
def DefaultLSFOptions():
	
	options = {}		
	options["cpumemory"] = 4000
	options["queue"] = '1nd'
		
	return options
		
def GetStatus(ID):
	
	command = ["bjobs", "-o", "stat", str(ID)]
	
	if sys.version_info[0] > 2:	
		process  = Popen(command, stdout=PIPE, stderr=PIPE, encoding='utf8')
	else:
		process  = Popen(command, stdout=PIPE, stderr=PIPE)
	out, err = process.communicate()
		
	if err == "Job <{0}> is not found\n".format(ID):
		status = "notfound"
	else:
		try:
			status = out.split("\n")[1].replace(" ","").lower()
			if status == "pend":
				status = "pending"
			elif status == "run":
				status = "running"
			elif status == "done":
				status = "completed"
			elif status == "exit" or status == "ususp" or status == "ssusp":
				status = "cancelled"
			elif status == "unkwn" or status == "zombi":
				status = "failed"
		except IndexError:
			status = "pending"
			
	return status
	
	#### put a try and catch
	
class DeliveryClerk(object):
	
	def __init__(self, **kwargs):
		
		default_options = DefaultLSFOptions()
		self.default_options = default_options
		
		self.defaults = []
		options = {}
				
		options["subtime"] = kwargs.get("subtime", [0, 23])
				
		options["cpumemory"] = kwargs.get("cpumemory", default_options['cpumemory'])
		self.defaults += ["cpumemory"]
		
		options["queue"] = kwargs.get("queue", default_options['queue'])
		self.defaults += ["queue"]
		
		self.options = options
		
		self.addvar("cpu_memory")
		self.addvar("queue", allowed_values = ["8nm","1nh","8nh","1nd","2nd","1nw","2nw"])
		
	
	def outdict(self):
		return {"options": self.options}
		
		
	@classmethod
	def from_dict(cls, dict, **kwargs):
		deliveryclerk = cls(**dict["options"])	
		
		return deliveryclerk
		
				
	def send_job(self, job):
		for n in job.range_subjobs:	
			job[n].send()
			
						
	def send_subjob(self, subjob):
		if not subjob._status.submitted or subjob._status.failed:
			if subjob._status.failed:
				subjob.reset()
			
			send_options = subjob.send_options
			send_options["lsf"] = True
			subjobid = submit(**send_options)
			
			return subjobid
			
	
	def get_update_subjobs(self, job):
		return None
		
	def getstatus(self, ID):
		return GetStatus(ID)
		
	def clear(self, job):
		pass
		
	def kill(self, **kwargs):
		return True
		
	def killsubjob(self, ID):
		Kill(ID)
				
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
	
	
