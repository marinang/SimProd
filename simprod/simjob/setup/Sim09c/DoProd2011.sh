#!/bin/bash

#sim09c
#from https://its.cern.ch/jira/browse/LHCBGAUSS-1186
#Stripping 21r1

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4
Turbo=$5
muDST=$6
Stripping=$7
ReDecay=$8

if [ "$Polarity" == "MagUp" ]; then
  SimCond=Gauss/Sim08-Beam3500GeV-mu100-2011-nu2.py
  DBtag="sim-20160614-1-vc-mu100"
elif [ "$Polarity" == "MagDown" ]; then
  SimCond=Gauss/Sim08-Beam3500GeV-md100-2011-nu2.py
  DBtag="sim-20160614-1-vc-md100"
else
  echo "Error, Polarity '$Polarity' is not valid!" 
  exit 1
fi

DDDBtag="dddb-20170721-1"

CONDITIONS=$PWD/Conditions.py

# Prepare conditions
echo "from Configurables import LHCbApp" >> $CONDITIONS
echo "LHCbApp().DDDBtag   = '$DDDBtag'" >> $CONDITIONS
echo "LHCbApp().CondDBtag = '$DBtag'" >> $CONDITIONS

#-------------# 
#   GAUSS     #
#-------------#

GAUSSJOB=$PWD/Gauss-Job.py
GAUSSOUTPUT=$PWD/Gauss.sim

# Prepare files
echo "from Gauss.Configuration import *" >> $GAUSSJOB
echo "GaussGen = GenInit('GaussGen')"    >> $GAUSSJOB
echo "GaussGen.FirstEventNumber = 1"     >> $GAUSSJOB
echo "GaussGen.RunNumber = $RunNumber"   >> $GAUSSJOB
echo "LHCbApp().EvtMax = $Nevents"       >> $GAUSSJOB
echo "from Configurables import OutputStream" >> $GAUSSJOB
echo "OutputStream('GaussTape').Output = \"DATAFILE='PFN:$GAUSSOUTPUT' TYP='POOL_ROOTTREE' OPT='RECREATE'\"" >> $GAUSSJOB

# Run

if [ "$ReDecay" == "True" ]; then
  lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r342" Gauss/v49r8 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/DataType-2011.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/NoPacking.py \$LBPYTHIA8ROOT/options/Pythia8_7TeV.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \$APPCONFIGOPTS/Gauss/ReDecay-100times.py \$$PPCONFIGOPTS/Gauss/ReDecay-SignalRepeatedHadronization-fix.py $Optfile $CONDITIONS $GAUSSJOB
else
  lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r342" Gauss/v49r8 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/DataType-2011.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/NoPacking.py \$LBPYTHIA8ROOT/options/Pythia8_7TeV.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py $Optfile $CONDITIONS $GAUSSJOB
fi

rm $GAUSSJOB

#-------------#
#   BOOLE     #
#-------------#

BOOLEFILES=$PWD/Boole-Files.py
BOOLEOUTPUT=$PWD/Boole.digi

# Prepare files
echo "from Gaudi.Configuration import *" >> $BOOLEFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$GAUSSOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $BOOLEFILES

# Run
lb-run -c x86_64-slc6-gcc49-opt --use="AppConfig v3r342" Boole/v30r2p1 gaudirun.py \$APPCONFIGOPTS/Boole/Default.py \$APPCONFIGOPTS/Boole/DataType-2011.py \$APPCONFIGOPTS/Boole/NoPacking.py \$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py $CONDITIONS $BOOLEFILES

rm $GAUSSOUTPUT
rm $BOOLEFILES

#------------#
#     L0     #
#------------#

L0CONFIG=$PWD/L0Configuration.py
L0OUTPUT=$PWD/L0.digi

#Prepare special conditions
echo "from Gaudi.Configuration import *" > $L0CONFIG
echo "from Configurables import L0App" >> $L0CONFIG
echo "L0App().outputFile='$L0OUTPUT'" >> $L0CONFIG
echo "EventSelector().Input = [\"DATAFILE='PFN:$BOOLEOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $L0CONFIG

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r268" Moore/v20r4 gaudirun.py \$APPCONFIGOPTS/L0App/L0AppSimProduction.py \$APPCONFIGOPTS/L0App/DataType-2011.py \$APPCONFIGOPTS/L0App/L0AppTCK-0x0037.py $L0CONFIG $CONDITIONS

rm $BOOLEOUTPUT
rm $L0CONFIG

#------------#
#   MOORE    #
#------------#

MOORECONFIG=$PWD/MooreConfiguration.py
MOOREOUTPUT=$PWD/Moore.digi

# Prepare special conditions
echo "from Gaudi.Configuration import *" > $MOORECONFIG
echo "from Configurables import Moore" >> $MOORECONFIG
echo "Moore().DDDBtag   = '$DDDBtag'" >> $MOORECONFIG
echo "Moore().CondDBtag = '$DBtag'" >> $MOORECONFIG
echo "Moore().UseDBSnapshot = False" >> $MOORECONFIG
echo "EventSelector().Input = [\"DATAFILE='PFN:$L0OUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $MOORECONFIG
echo "Moore().outputFile = '$MOOREOUTPUT'" >> $MOORECONFIG

# Run
lb-run -c x86_64-slc5-gcc43-opt --use="AppConfig v3r268" Moore/v12r8g3 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep.py \$APPCONFIGOPTS/Conditions/TCK-0x40760037.py \$APPCONFIGOPTS/Moore/DataType-2011.py $MOORECONFIG $CONDITIONS

rm $L0OUTPUT
rm $MOORECONFIG

#-------------#
#   BRUNEL    #
#-------------#

BRUNELFILES=$PWD/Brunel-Files.py
BRUNELOUTPUT=$PWD/Brunel.dst

# Prepare files
echo "from Gaudi.Configuration import *" >> $BRUNELFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$MOOREOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $BRUNELFILES

# Run
lb-run -c x86_64-slc5-gcc46-opt --use="AppConfig v3r302" Brunel/v43r2p11 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2011.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Brunel/Sim09-Run1.py \$APPCONFIGOPTS/Persistency/DST-multipleTCK-2011.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $BRUNELFILES $CONDITIONS

rm $MOOREOUTPUT
rm $BRUNELFILES

#------------------------#
#   DAVINCI/STRIPPING    #
#------------------------#

DAVINCIFILES=$PWD/DaVinci-Files.py

# Prepare files
echo "from Gaudi.Configuration import *" >> $DAVINCIFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$BRUNELOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $DAVINCIFILES

lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r338" DaVinci/v36r1p5 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping21r1-Stripping-MC-NoPrescaling.py \$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py \$APPCONFIGOPTS/DaVinci/DataType-2011.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py $CONDITIONS $DAVINCIFILES

# Run

rm $BRUNELOUTPUT
rm $DAVINCIFILES

rm *.root
rm *.py

rm test_catalog.xml
rm NewCatalog.xml

mv *AllStreams.dst ${Nevents}_events.dst

# Finish

# EOF

# EOF
