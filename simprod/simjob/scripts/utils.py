#!/usr/bin/python

from subprocess import Popen, PIPE

# Definition of handy colours for printing
_default    = '\x1b[00m'
_green      = '\x1b[01;32m'
_red        = '\x1b[01;31m'
_blue       = '\x1b[01;34m'
_magenta    = '\x1b[1;35m'
_cyan       = '\x1b[01;36m'
_yellow     = '\x1b[01;33m'

def cdefault( text ):
	return "{0}{1}{2}".format( _default, text, _default)

def green( text ):
	return "{0}{1}{2}".format( _green, text, _default)
	
def red( text ):
	return "{0}{1}{2}".format( _red, text, _default)
	
def blue( text ):
	return "{0}{1}{2}".format( _blue, text, _default)
	
def magenta( text ):
	return "{0}{1}{2}".format( _magenta, text, _default)
	
def cyan( text ):
	return "{0}{1}{2}".format( _cyan, text, _default)
	
def yellow( text ):
	return "{0}{1}{2}".format( _yellow, text, _default)
	
def baserunnumber():
	from datetime import datetime
	now = datetime.now()
	
	minute = now.minute
	hour   = now.hour
	day    = now.day
	month  = now.month
	
	if month == 11:
		month = 1
		day  += 31
	elif month == 12:
		month = 2
		day  += 31
	
	return (minute + 100*hour + 10000*day + 1000000*month) * 100
	
def silentrm( path ):
	
	
	
	P = Popen(['rm','-rf',path], stdout=PIPE, stderr=PIPE)
	_, _ = P.communicate()