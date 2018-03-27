#!/bin/bash

#sim09c
#from https://its.cern.ch/jira/browse/LHCBGAUSS-1186
#Stripping 21r1

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4

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
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r342" Gauss/v49r8 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/DataType-2011.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/NoPacking.py \$LBPYTHIA8ROOT/options/Pythia8_7TeV.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py $Optfile Conditions.py Gauss-Job.py

# Prepare output
mv `ls *.sim` Gauss.sim
rm Gauss-Job.py

#-------------#
#   BOOLE     #
#-------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> Boole-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Gauss.sim' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Boole-Files.py

# Run
lb-run -c x86_64-slc6-gcc49-opt gaudirun.py --use="AppConfig v3r342" Boole/v30r2p1 gaudirun.py \$APPCONFIGOPTS/Boole/Default.py \$APPCONFIGOPTS/Boole/DataType-2011.py \$APPCONFIGOPTS/Boole/NoPacking.py \$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py Conditions.py Boole-Files.py

rm Gauss.sim
rm Boole-Files.py

#------------#
#     L0     #
#------------#

export CMTCONFIG=x86_64-slc5-gcc46-opt
source LbLogin.sh -c x86_64-slc5-gcc46-opt
source SetupProject.sh Moore v20r4 --use "AppConfig v3r200"

#Prepare special conditions
echo "from Gaudi.Configuration import *" > L0Configuration.py
echo "from Configurables import L0App" >> L0Configuration.py
echo 'L0App().outputFile="L0.digi"' >> L0Configuration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Boole.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> L0Configuration.py

# Run
lb-run -c x86_64-slc5-gcc43-opt --use="AppConfig v3r268" Moore/v20r4 gaudirun.py $APPCONFIGOPTS/L0App/L0AppSimProduction.py $APPCONFIGOPTS/L0App/DataType-2011.py $APPCONFIGOPTS/L0App/L0AppTCK-0x0037.py L0Configuration.py

rm Boole.digi
rm L0Configuration.py

#------------#
#   MOORE    #
#------------#

# Prepare special conditions
echo "from Gaudi.Configuration import *" > MooreConfiguration.py
echo "from Configurables import Moore" >> MooreConfiguration.py
echo "Moore().DDDBtag   = '$DDDBtag'" >> MooreConfiguration.py
echo "Moore().CondDBtag = '$DBtag'" >> MooreConfiguration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./L0.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> MooreConfiguration.py
echo "Moore().outputFile = 'Moore.digi'" >> MooreConfiguration.py

# Run
lb-run -c x86_64-slc5-gcc43-opt --use="AppConfig v3r268" Moore/v12r8g3 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep.py \$APPCONFIGOPTS/Conditions/TCK-0x40760037.py \$APPCONFIGOPTS/Moore/DataType-2011.py MooreConfiguration.py

rm L0.digi
rm MooreConfiguration.py

#-------------#
#   BRUNEL    #
#-------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> Brunel-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Moore.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Brunel-Files.py

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r302" Brunel/v43r2p11 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2011.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Brunel/Sim09-Run1.py \$APPCONFIGOPTS/Persistency/DST-multipleTCK-2011.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Brunel-Files.py Conditions.py

rm Moore.digi
rm Brunel-Files.py

#------------------------#
#   DAVINCI/STRIPPING    #
#------------------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> DaVinci-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Brunel.dst' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> DaVinci-Files.py

lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r338" DaVinci/v36r1p5 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping21r1-Stripping-MC-NoPrescaling.py \$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py \$APPCONFIGOPTS/DaVinci/DataType-2011.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py Conditions.py DaVinci-Files.py

# Run

rm DaVinci-Files.py

rm *.root
rm *.py

rm test_catalog.xml
rm NewCatalog.xml

mv *AllStreams.dst ${Nevents}_events.dst

# Finish

# EOF
