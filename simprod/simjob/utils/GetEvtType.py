#!/usr/bin/python
# -*- coding: utf-8 -*-

## Author: Matthieu Marinangeli
## Mail: matthieu.marinangeli@cern.ch
## Description: copy the all options files related to an EvtType in a directory called EvtTypes.
## The users can they modify as they want these options files.

import argparse
import os
import shutil
import sys


def getevttype(evttype, decfiles="v30r25"):

    Options = {"evttype": evttype, "decfiles": decfiles}

    moddir = os.getenv("SIMPRODPATH")

    decfiles_path = "/cvmfs/lhcb.cern.ch/lib/lhcb/DBASE/Gen/DecFiles/{decfiles}".format(
        **Options
    )

    if not os.path.isdir(decfiles_path):
        raise NotImplementedError("This DecFiles package version does not exist!")

    optfile = "{0}/options/{evttype}.py".format(decfiles_path, **Options)

    if not os.path.isfile(optfile):
        raise NotImplementedError("The evttype {0} does not exist!".format(evttype))

    if not os.path.isdir("{0}/EvtTypes".format(moddir)):
        os.makedirs("{0}/EvtTypes".format(moddir))
    if not os.path.isdir("{0}/EvtTypes/{evttype}".format(moddir, **Options)):
        os.makedirs("{0}/EvtTypes/{evttype}".format(moddir, **Options))

    with open(optfile, "r") as file:
        lines = file.readlines()

    decfileroot_files = []

    for i, l in enumerate(lines):
        if "DECFILESROOT" in l:
            decfile = l.split("DECFILESROOT")[-1]
            decfile = decfile.split('"')[0]
            decfile = decfile.replace('"\n', "")
            decfileroot_files.append({"file": decfile, "index": i})

    for f in decfileroot_files:
        filename = f["file"].split("/")[-1]
        index = f["index"]
        shutil.copyfile(
            "{0}/{1}".format(decfiles_path, f["file"]),
            "{0}/EvtTypes/{evttype}/{1}".format(moddir, filename, **Options),
        )

        # modify the locations in the option file
        lines[index] = lines[index].replace(
            "$DECFILESROOT{0}".format(f["file"]),
            "{0}/EvtTypes/{evttype}/{1}".format(moddir, filename, **Options),
        )

    OptFile = "{0}/EvtTypes/{evttype}/{evttype}.py".format(moddir, **Options)

    with open(OptFile, "w") as file:
        file.writelines(lines)
