#!/usr/bin/python
# -*- coding: utf-8 -*-


class NotPreparedError(Exception):
    """Exception class for jobs not prepared"""

    pass


class SubmittedError(Exception):
    """Exception class for modifying a subjob attributed after being submitted"""

    pass


class PreparedError(Exception):
    """Exception class for modifying a job attributed after being prepared"""

    pass
