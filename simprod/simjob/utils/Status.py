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

"""
Allowed status for subjobs:
    * new
    * submitted
    * running
    * completed
    * failed
    * notfound
    * error
"""


def valid_output(output):
    if os.path.isfile(output) and os.path.getsize(output) >= 700000:
        return True
    else:
        return False


def resolve_status(previous_status, status, output):

    if previous_status == "new":
        allowed_status = ["submitted", "running"]
        if status in allowed_status:
            return status
        if status == "completed":
            if valid_output(output):
                return status
            else:
                return "failed"
        else:
            return previous_status
    else:
        if status in ["completed", "notfound", "error", "failed"]:
            if valid_output(output):
                return status
            else:
                return "failed"
        else:
            return status
