#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Matthieu Marinangeli
# Mail: matthieu.marinangeli@cern.ch
# Description: get status of jobs for the current submission

import os
import datetime
import sys

TIME_NEW = 60  # minutes, time between check of status if status is new
TIME_RUNNING = 15
TIME_FAILED = 35
TIME_SUBMITTED = 5


py3 = (
    sys.version_info[0] > 2
)  # creates boolean value for test that Python major version > 2


class Status(object):
    def __init__(self, status, output, in_init=False):

        self.in_init = in_init
        self.status = "new"

        if os.path.isfile(output):
            if os.path.getsize(output) >= 700000:
                self.status = "completed"
            else:
                self.status = "failed"

        else:
            if status in ["submitted", "running"]:
                self.status = status

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

        types = [str]
        if not py3:
            types.append(unicode)

        if isinstance(other, Status):
            return self.status == other.status
        elif isinstance(other, tuple(types)):
            return self.status == other
        else:
            raise ValueError(
                "Cannot compare {0} and {1}.".format(type(self), type(other))
            )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.status
