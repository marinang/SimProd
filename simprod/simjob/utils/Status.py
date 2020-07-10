#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Matthieu Marinangeli
# Mail: matthieu.marinangeli@cern.ch
# Description: get status of jobs for the current submission

import os
import datetime
import sys

TIME_NEW = 1  # minutes, time between check of status if status is new
TIME_RUNNING = 5
TIME_FAILED = 10
TIME_SUBMITTED = 1


py3 = (
    sys.version_info[0] > 2
)  # creates boolean value for test that Python major version > 2


class Status(object):
    def __init__(self, status, output, in_init=False):

        self.in_init = in_init
        
        if status in ["new", "submitted", "running", "failed"]:
            self.status = status
        else:
            if os.path.isfile(output) and os.path.getsize(output) >= 700000:
                self.status = "completed"
            else:
                self.status = "failed"

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
