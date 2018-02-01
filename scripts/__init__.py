#!/usr/bin/python

from .SlurmSubCondition import *
from .GetEvtType import *
from .submit import main as submit

# Definition of handy colours for printing
_default    = '\x1b[00m'
_green      = '\x1b[01;32m'
_red        = '\x1b[01;31m'
_blue       = '\x1b[01;34m'
_magenta    = '\x1b[1;35m'
_cyan       = '\x1b[01;36m'
_yellow     = '\x1b[01;33m'

def green( text ):
	return "{0} {1} {2}".format( _green, text, _default)
	
def red( text ):
	return "{0} {1} {2}".format( _red, text, _default)
	
def blue( text ):
	return "{0} {1} {2}".format( _blue, text, _default)
	
def magenta( text ):
	return "{0} {1} {2}".format( _magenta, text, _default)
	
def cyan( text ):
	return "{0} {1} {2}".format( _cyan, text, _default)
	
def yellow( text ):
	return "{0} {1} {2}".format( _yellow, text, _default)
