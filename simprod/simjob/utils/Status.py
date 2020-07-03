#!/usr/bin/python
# -*- coding: utf-8 -*-

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: get status of jobs for the current submission

import glob
import os
from .utilities import *
import time
import subprocess
import datetime

TIME_NEW = 60  # minutes, time between check of status if status is new
TIME_RUNNING = 15
TIME_FAILED = 35
TIME_SUBMITTED = 5
DEBUG = 0


class Status(object):
    def __init__(self, status, output, in_init=False):

        self.submitted = False
        self.running = False
        self.finished = False
        self.completed = False
        self.failed = False
        self.in_init = in_init

        self.status = status
        self.output = output

        if status in "submitted":
            self.submitted = True

        if status == "running":
            self.running = True
            self.submitted = True

        elif (
            status == "completed"
            or status == "cancelled"
            or status == "failed"
            or status == "notfound"
        ):
            self.running = False
            self.finished = True
            self.submitted = True

        if output != "" and os.path.isfile(output):
            if os.path.isfile(output) and os.path.getsize(output) >= 700000:
                self.completed = True
            elif os.path.isfile(output) and os.path.getsize(output) < 700000:
                self.failed = True
            elif self.output == "":
                self.failed = True
        elif status == "notfound":
            self.failed = True

        if not self.submitted:
            self.status = "new"
        elif self.submitted and not self.running and not self.finished:
            self.status = "submitted"
        elif self.submitted and self.running and not self.finished:
            self.status = "running"
        elif self.submitted and not self.running and self.finished:
            if self.completed:
                self.status = "completed"
            elif self.failed:
                self.status = "failed"

        self.creation_time = datetime.datetime.now()

        if DEBUG > 0:
            print(
                "In Status.__init__, status={0}, time={1}".format(
                    status, self.creation_time
                )
            )

    @property
    def isvalid(self):

        if self.in_init:
            return False

        if self.status == "new":
            delta = TIME_NEW
        elif self.status == "running":
            delta = TIME_RUNNING
        elif self.status == "failed":
            delta = TIME_FAILED
        elif self.status == "submitted":
            delta = TIME_SUBMITTED
        else:
            delta = 2

        now = datetime.datetime.now()
        elapsedTime = now - self.creation_time
        minutes = divmod(elapsedTime.total_seconds(), 60)[0]

        valid = minutes < delta

        if DEBUG > 0:
            print(
                "In Status.isvalid: Delta={0}; elapsed time={1}, valid={2}".format(
                    delta, minutes, valid
                )
            )

        return valid

    def __eq__(self, other):
        if isinstance(other, Status):
            return self.status == other.status
        elif isinstance(other, str):
            return self.status == other
        else:
            raise ValueError()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.status


def GetStatus(Job):

    JobID = Job["jobid"]

    ### Slurm
    try:
        subprocess.Popen(["squeue"], stdout=subprocess.PIPE)
    except OSError:
        Slurm = False
    else:
        Slurm = True

    if Slurm:

        ntries = 20
        n = 0
        while n < ntries:
            process = subprocess.Popen(
                ["sacct", "-j", str(JobID), "--format=State"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            out, err = process.communicate()
            status = out.split("\n")[-2].replace(" ", "").lower()

            if status == "----------":
                time.sleep(0.5)
            else:
                break

        if status == "----------":
            raise NotImplementedError("Job not found")

        return status

    elif "lxplus" in os.getenv("HOSTNAME"):
        return NotImplemented


def SetStatus(Jobs):

    nthisjob = Jobs["nthisjob"]
    njobs = Jobs["njobs"]

    for i in range(nthisjob):

        job = Jobs[str(i)]

        if job["completed"] or job["failed"]:
            continue

        job["submitted"] = True

        IsRunning(job)

        IsCompleted(job)

        IsFailed(job)

        WriteStatus(job)


def WriteStatus(Job):

    JobDirectory = Job["production_folder"]

    status_file = "{0}/status".format(JobDirectory)

    if os.path.isfile(status_file):
        os.remove(status_file)

    status_file = open(status_file, "w")
    status_file.write("submitted: {0}\n".format(Job["submitted"]))
    status_file.write("running: {0}\n".format(Job["running"]))
    status_file.write("completed: {0}\n".format(Job["completed"]))
    status_file.write("failed: {0}\n".format(Job["failed"]))
    status_file.close()


def IsRunning(Job):

    if Job["submitted"]:
        if GetStatus(Job) == "running":
            Job["running"] = True
        else:
            Job["running"] = False


def IsCompleted(Job):

    if Job["submitted"] and IsFinished(Job):
        JobDirectory = Job["production_folder"]

        if os.path.isdir(JobDirectory):
            dst = JobDirectory + "/" + Job["production_file"]

            if os.path.isfile(dst) and os.path.getsize(dst) > 1000000:
                Job["completed"] = True

        elif IsMoved(Job):
            Job["completed"] = True


def IsFailed(Job):

    if Job["submitted"] and IsFinished(Job):
        JobDirectory = Job["production_folder"]

        if os.path.isdir(JobDirectory):
            dst = JobDirectory + "/" + Job["production_file"]

            if os.path.isfile(dst) and os.path.getsize(dst) < 1000000:
                Job["failed"] = True
            elif not os.path.isfile(dst):
                Job["failed"] = True


def IsFinished(Job):

    if Job["submitted"] and not Job["completed"] and not Job["failed"]:
        completed = GetStatus(Job) == "completed"
        canceled = GetStatus(Job) == "canceled"
        failed = GetStatus(Job) == "failed"

        if completed or canceled or failed:
            return True
        else:
            return False


def IsMoved(Job):

    JobDirectory = Job["production_folder"]
    Destination = Job["destination_folder"]
    File = Destination + "/" + Job["destination_file"]

    if os.path.isdir(JobDirectory):
        return False
    else:
        if os.path.isfile(File):
            return True
        else:
            raise (NotImplementedError("File is lost!"))
