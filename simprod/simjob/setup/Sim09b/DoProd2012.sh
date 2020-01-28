#!/bin/bash

#from https://its.cern.ch/jira/browse/LHCBGAUSS-957
#Stripping 21

. /cvmfs/lhcb.cern.ch/lib/LbEnv

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4
Turbo=$5
muDST=$6
Stripping=$7

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

DDDBtag="dddb-20150928"

# Prepare conditions
echo "from Configurables import LHCbApp" >> Conditions.py
echo "LHCbApp().DDDBtag   = '$DDDBtag'" >> Conditions.py
echo "LHCbApp().CondDBtag = '$DBtag'" >> Conditions.py

#-------------# 
#   GAUSS     #
#-------------#

export CMTCONFIG=x86_64-slc6-gcc48-opt
source LbLogin.sh -c x86_64-slc6-gcc48-opt
source SetupProject.sh Gauss v49r7 --use "AppConfig v3r277"

# Prepare files
echo "from Gauss.Configuration import *" >> Gauss-Job.py
echo "GaussGen = GenInit('GaussGen')"    >> Gauss-Job.py
echo "GaussGen.FirstEventNumber = 1"     >> Gauss-Job.py
echo "GaussGen.RunNumber = $RunNumber"   >> Gauss-Job.py
echo "LHCbApp().EvtMax = $Nevents"       >> Gauss-Job.py

# Run
gaudirun.py $APPCONFIGOPTS/$SimCond $APPCONFIGOPTS/Gauss/DataType-2012.py $APPCONFIGOPTS/Gauss/RICHRandomHits.py $APPCONFIGOPTS/Gauss/NoPacking.py $LBPYTHIA8ROOT/options/Pythia8.py $APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $Optfile Conditions.py Gauss-Job.py

# Prepare output
mv `ls *.sim` Gauss.sim
rm Gauss-Job.py

#-------------#
#   BOOLE     #
#-------------#

export CMTCONFIG=x86_64-slc6-gcc48-opt
source LbLogin.sh -c x86_64-slc6-gcc48-opt
source SetupProject.sh Boole v30r1 --use "AppConfig v3r266"

# Prepare files
echo "from Gaudi.Configuration import *" >> Boole-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Gauss.sim' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Boole-Files.py

# Run
gaudirun.py $APPCONFIGOPTS/Boole/Default.py $APPCONFIGOPTS/Boole/DataType-2012.py $APPCONFIGOPTS/Boole/NoPacking.py $APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Conditions.py Boole-Files.py

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
gaudirun.py $APPCONFIGOPTS/L0App/L0AppSimProduction.py $APPCONFIGOPTS/L0App/DataType-2012.py $APPCONFIGOPTS/L0App/L0AppTCK-0x0045.py L0Configuration.py

rm Boole.digi
rm L0Configuration.py

#------------#
#   MOORE    #
#------------#

export CMTCONFIG=x86_64-slc5-gcc46-opt
source LbLogin.sh -c x86_64-slc5-gcc46-opt
source SetupProject.sh Moore v14r8p1 --use "AppConfig v3r263"

# Prepare special conditions
echo "from Gaudi.Configuration import *" > MooreConfiguration.py
echo "from Configurables import LHCbApp, Moore" >> MooreConfiguration.py
echo "LHCbApp().DDDBtag   = '$DDDBtag'" >> MooreConfiguration.py
echo "LHCbApp().CondDBtag = '$DBtag'" >> MooreConfiguration.py
echo "Moore().DDDBtag   = '$DDDBtag'" >> MooreConfiguration.py
echo "Moore().CondDBtag = '$DBtag'" >> MooreConfiguration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./L0.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> MooreConfiguration.py
echo "Moore().outputFile = 'Moore.digi'" >> MooreConfiguration.py

# Run
gaudirun.py $APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep.py $APPCONFIGOPTS/Conditions/Transform-0x409f0045-NoRichPIDLines.py $APPCONFIGOPTS/Moore/DataType-2012.py MooreConfiguration.py

rm L0.digi
rm MooreConfiguration.py

#-------------#
#   BRUNEL    #
#-------------#

export CMTCONFIG=x86_64-slc5-gcc46-opt
source LbLogin.sh -c x86_64-slc5-gcc46-opt
source SetupProject.sh Brunel v43r2p11 --use "AppConfig v3r307"

# Prepare files
echo "from Gaudi.Configuration import *" >> Brunel-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Moore.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Brunel-Files.py

# Run
gaudirun.py $APPCONFIGOPTS/Brunel/DataType-2012.py $APPCONFIGOPTS/Brunel/MC-WithTruth.py $APPCONFIGOPTS/Brunel/Sim09-Run1.py $APPCONFIGOPTS/Persistency/DST-multipleTCK-2012.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Brunel-Files.py Conditions.py

rm Moore.digi
rm Brunel-Files.py

#------------------------#
#   DAVINCI/STRIPPING    #
#------------------------#

export CMTCONFIG=x86_64-slc6-gcc48-opt
source LbLogin.sh -c x86_64-slc6-gcc48-opt
source SetupProject.sh DaVinci v36r1p3 --use "AppConfig v3r277"

# Prepare files
echo "from Gaudi.Configuration import *" >> DaVinci-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Brunel.dst' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> DaVinci-Files.py

# Run
gaudirun.py $APPCONFIGOPTS/DaVinci/DV-Stripping21-Stripping-MC-NoPrescaling.py $APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py $APPCONFIGOPTS/DaVinci/DataType-2012.py $APPCONFIGOPTS/DaVinci/InputType-DST.py Conditions.py DaVinci-Files.py

rm Brunel.dst
rm DaVinci-Files.py

rm *.root
rm *.py

rm test_catalog.xml
rm NewCatalog.xml

mv *AllStreams.dst ${Nevents}_events.dst

# Finish
# EOF
