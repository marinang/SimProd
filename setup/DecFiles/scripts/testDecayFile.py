#!/usr/bin/env python
'''Script, which run nightlies test of single decay file. Can be used also
for locally to replicate test. It will use DECFILESROOT equal to directory
from which script is called.'''

from __future__ import print_function
import sys, os
import math
import subprocess
import tempfile
import logging

##############################################

def testEventType(eventType, nevents=0):
    '''Function, which runs actual test for given event type.'''
    gaussVersion = 'v49r8'
    fullPath = sys.argv[0]
    if fullPath[0] != '/':
        fullPath = os.getcwd()+'/'+sys.argv[0]
    # Now work out DecFiles path
    tmpList = fullPath.strip().split('/')
    decFilesRoot = '/'
    for i in range(1, len(tmpList) - 2):
        if tmpList[i] != '.':
            decFilesRoot += tmpList[i] + '/'
    os.environ['DECFILESROOT'] = decFilesRoot
    # find out CPU time
    cpuTime = findCPUTime(eventType)
    (numEvents, timeLimit) = testSize(cpuTime, nevents)
    generator = '$LBPYTHIA8ROOT/options/Pythia8.py'
    if eventType[0:2] == '14':
        generator = '$LBBCVEGPYROOT/options/BcVegPyPythia8.py'
    if eventType[0:2] == '26' and (eventType[6] == '5' or eventType[6] == '6'):
        generator = '$LBGENXICCROOT/options/GenXiccPythia8.py'
    if eventType[0:2] == '16' and (eventType[6] == '6'):
        generator = '$LBGENXICCROOT/options/GenXibc.py'
    if eventType[0:2] == '26' and (eventType[6] == '8' or eventType[6] == '9'):
        generator = '$LBPYTHIA8ROOT/options/Pythia8.py'
    if eventType[0:1] == '4':
        generator = productionToolFor4(eventType)
    # Now we have all we need, so can start to construct test command
    # First write option file to set number of events to run
    nevtFile = tempfile.mkstemp(suffix='.py')
    os.write(nevtFile[0], '''from Gauss.Configuration import *

#--Generator phase, set random numbers
GaussGen = GenInit("GaussGen")
GaussGen.FirstEventNumber = 1
GaussGen.RunNumber        = 1082

#--Number of events
# We will set number of events separately in other file, we want to make
# sure we pick right number.
nEvts = '''+str(numEvents)+'''
LHCbApp().EvtMax = nEvts
''')
    os.close(nevtFile[0])
    # Now construct full test command. Under lb-run we need to first set
    # DECFILESROOT and then run Gauss.
    runFile = tempfile.mkstemp(suffix='.sh')
    os.write(runFile[0], 'export DECFILESROOT='+decFilesRoot+'''
env|grep DECFILESROOT
cat ''' + nevtFile[1] + '''
ulimit -t ''' + str(int(timeLimit)) + '''
gaudirun.py $GAUSSOPTS/Gauss-2012.py \
            $DECFILESROOT/options/'''+eventType+'''.py \
            ''' + generator + ''' \
            $GAUSSOPTS/GenStandAlone.py \
            $GAUSSROOT/tests/options/testGauss-NoOutput.py \
            ''' + nevtFile[1])
    os.close(runFile[0])

#    runCommand = ['lb-run --nightly=lhcb-sim09 Gauss ' + gaussVersion + ' bash ' + runFile[1]]
    runCommand = ['lb-run Gauss/' + gaussVersion + ' bash ' + runFile[1]]
    # Here we can do actual running of Gauss and grabbing stdout and stderr
    proc = subprocess.Popen(runCommand, shell=True, \
               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Get hold of stdout and stderr (need to discuss with Marco what I should
# do with it for nightlies as he might want to get it to show it on web)
    (sout, serr) = proc.communicate()
#    print(sout)
#    print(serr)
    os.remove(nevtFile[1])
    os.remove(runFile[1])
    # Finally work out whether test succeeded or not
    # expected strings
    expString1 = 'Application Manager Terminated successfully'
    expString2 = str(numEvents) + ' events processed'
    nFound = 0
    if sout.find(expString1) > -1:
        nFound += 1
    if sout.find(expString2) > -1:
        nFound += 1
    if nFound == 2:
        return True, sout, serr
    return False, sout, serr

##############################################

def findCPUTime(eventType):
    '''Function, which finds for given event type CPUTime from
corresponding decay file.'''
    # First we need to find dec file from options file
    fileName = os.environ['DECFILESROOT']+'/options/'+eventType+".py"
    if not os.path.exists(fileName):
        logging.error('Option file '+fileName+' not found.')
        return 60
    optionFile = open(fileName)
    decayFileName = ""
    for line in optionFile:
        if line.find('EvtGenDecay.UserDecayFile') != -1:
            splitted = line.split('"')
            if len(splitted) < 2:
                print("Something is wrong in option file:", fileName)
            decayFileName = splitted[1]
            break
    optionFile.close()
    decayFileName = decayFileName.replace('$DECFILESROOT', os.environ['DECFILESROOT'])
    # Now we go through decay file and find CPU time. For now, if we do not
    # find field, return 1 min as default. On return we convert to seconds.
    if not os.path.exists(decayFileName):
        logging.error('Decay file '+decayFileName+' not found.')
        return 60
    decFile = open(decayFileName)
    for line in decFile:
        if line.find('CPUTime') != -1:
            splitted = line.split(':')
            if len(splitted) < 2:
                print("Missing CPUTime in decay file ", decayFileName)
            time = splitted[1]
            unitStart = None
            unit = 60
            unitStart = time.find('min')
            if unitStart == -1:
                unitStart = time.find('s')
                unit = 1
                # Safety net for case we cannot determine units
                if unitStart == -1:
                    return 1
            time = time[0:unitStart]
            # For case where we have <1min, we go for minute
            time = time.replace('<', '').strip()
            decFile.close()
            return math.ceil(convertTime(time))*unit
    # default value for now, before we get confident that this information
    # will always be there
    return 60

##############################################

def convertTime(s):
    '''Function to convert time to float while catching ValueError
exception.'''
    try:
        return float(s) # for int, long and float
    except ValueError:
        return 0
    return 0

##############################################

def testSize(cpuTime, nevents):
    '''Function which works out test time limit based on CPUTime and number
of events.'''
    # First handle case where we do not set number of events from outside
    if nevents <= 0:
        # Default number of events
        numEvents = 10
        # Maximum we can do in 30 minutes
        maxEvents = 30.*60/cpuTime
        if maxEvents < numEvents:
            if maxEvents >= 4:
                numEvents = maxEvents
            else:
                numEvents = 4
        # add 30% as safety margin for fluctuations
        timeLimit = numEvents * cpuTime * 1.3
        # Add another 240 seconds to allow for initialisations
        timeLimit += 240
        # if we go above 120 minutes, chop it down and if test fails, we will
        # anyhow require presentation of what user tries to do
        if timeLimit > 120*60:
            timeLimit = 120*60
    else:
        numEvents = nevents
        timeLimit = 1.3 * numEvents * cpuTime
    return (int(numEvents), timeLimit)

##############################################

def findProductionTool(fileName):
    '''Function which reads decay file and corresponding extra options to
find out which production tool should be used.'''
#    print 'Parsing file: ',fileName
    if not os.path.exists(fileName):
        logging.error('Option file '+fileName+' not found.')
        return  '$LBPYTHIA8ROOT/options/Pythia8.py'
    prodTool = '$LBPYTHIA8ROOT/options/Pythia8.py'
    optionFile = open(fileName)
    for line in optionFile:
        if line.find('Generation().Special.addTool') != -1:
            if line.find('Pythia8Production') != -1:
                optionFile.close()
                return '$LBPYTHIA8ROOT/options/Pythia8.py'
            elif line.find('OniaPairsProduction') != -1:
                optionFile.close()
                # Not perfect, but best without significant changes to
                # script
                return '$DECFILESROOT/options/LbOniaPsi1S1S.py'
            elif line.find('PowhegProduction') != -1:
                optionFile.close()
                return '$LBPOWHEGROOT/options/Powheg.py'
        if line.find('Generation.AlpGenDict') != -1:
            optionFile.close()
            return '$LBALPGENROOT/options/AlpGen.py'
        if line.find('importOptions') != -1:
            addFileName = ''
            splitter = '"'
            if line.find('\'') != -1:
                splitter = '\''
            addFileName = ''
            splittedLine = line.split(splitter)
            if len(splittedLine) > 1:
                addFileName = splittedLine[1]
            if fileName != addFileName and addFileName != '':
                addFileName = addFileName.replace('$DECFILESROOT', os.environ['DECFILESROOT'])
                prodTool = findProductionTool(addFileName)
            if prodTool != '$LBPYTHIA8ROOT/options/Pythia8.py':
                optionFile.close()
                return prodTool
    optionFile.close()
    return prodTool

##############################################

def productionToolFor4(eventType):
    '''Function which reads decay file and corresponding extra options to
find out which production tool should be used.'''
    fileName = os.environ['DECFILESROOT'] + '/options/' + eventType + ".py"
    return findProductionTool(fileName)

##############################################

if __name__ == '__main__':
    if len(sys.argv) < 2:
        os.exit()
    evtType = sys.argv[1]
    nevt = 0
    if len(sys.argv) == 3:
        nevt = int(sys.argv[2])
    result, out, err = testEventType(evtType, nevt)
    print('Result of the test for '+str(evtType)+' is ', result)
    if not result:
        print(out)
        print(err)
#    testEventType('12365400', 0)

