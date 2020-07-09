#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Matthieu Marinangeli
# Mail: matthieu.marinangeli@cern.ch
# Description: get status of jobs for the current submission

import os
import datetime

TIME_NEW = 60  # minutes, time between check of status if status is new
TIME_RUNNING = 15
TIME_FAILED = 35
TIME_SUBMITTED = 5


class Status(object):
    def __init__(self, status, output, in_init=False):

        self.submitted = False
        self.running = False
        self.finished = False
        self.completed = False
        self.failed = False
        self.in_init = in_init

        if status in "submitted":
            self.submitted = True

        if status == "running":
            self.running = True
            self.submitted = True

        if status in ["completed", "cancelled", "failed"]:
            self.running = False
            self.finished = True
            self.submitted = True
            
            if status == "failed":
                self.failed = True

        if output != "" and os.path.isfile(output):
            if os.path.isfile(output) and os.path.getsize(output) >= 700000:
                self.completed = True
            elif os.path.isfile(output) and os.path.getsize(output) < 700000:
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
