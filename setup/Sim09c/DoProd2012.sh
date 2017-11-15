#!/bin/bash

#sim09c
#from https://its.cern.ch/jira/browse/LHCBGAUSS-1185
#Stripping 21

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4

if [ "$Polarity" == "MagUp" ]; then
  SimCond=Gauss/Sim08-Beam4000GeV-mu100-2012-nu2.5.py
  DBtag="sim-20160321-2-vc-mu100"
elif [ "$Polarity" == "MagDown" ]; then
  SimCond=Gauss/Sim08-Beam4000GeV-md100-2012-nu2.5.py
  DBtag="sim-20160321-2-vc-md100"
else
  echo "Error, Polarity '$Polarity' is not valid!" 
  exit 1
fi

DDDBtag="dddb-20170721-2"

# Prepare conditions
echo "from Configurables import LHCbApp" >> Conditions.py
echo "LHCbApp().DDDBtag   = '$DDDBtag'" >> Conditions.py
echo "LHCbApp().CondDBtag = '$DBtag'" >> Conditions.py

#-------------# 
#   GAUSS     #
#-------------#


# Prepare files
echo "from Gauss.Configuration import *" >> Gauss-Job.py
echo "GaussGen = GenInit('GaussGen')"    >> Gauss-Job.py
echo "GaussGen.FirstEventNumber = 1"     >> Gauss-Job.py
echo "GaussGen.RunNumber = $RunNumber"   >> Gauss-Job.py
echo "LHCbApp().EvtMax = $Nevents"       >> Gauss-Job.py

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r342" Gauss/v49r8 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/DataType-2012.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/NoPacking.py \$LBPYTHIA8ROOT/options/Pythia8.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py $Optfile Conditions.py Gauss-Job.py

# Prepare output
mv `ls *.sim` Gauss.sim
rm Gauss-Job.py

#-------------#
#   BOOLE     #
#-------------#
