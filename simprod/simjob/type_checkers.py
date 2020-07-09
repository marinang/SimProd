#!/usr/bin/python

def check_nevents(nevents):
    
    if isinstance(nevents, (int, float)):
        nevents = int(nevents)
        return nevents
    else:
        raise TypeError("nevents must be a int!")