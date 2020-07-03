#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil


def Move(initial_file, destination_file):

    destination_dir = os.path.dirname(destination_file)

    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)

    shutil.move(initial_file, destination_file)


def EosMove(initial_file, destination_file):

    destination_dir = os.path.dirname(destination_file)

    if not os.path.isdir(destination_dir):
        os.system("xrdfs root://eoslhcb.cern.ch/ mkdir -p {0}".format(destination_dir))

    os.system(
        "xrdfs root://eoslhcb.cern.ch/ mv {0} {1}".format(
            initial_file, destination_file
        )
    )
