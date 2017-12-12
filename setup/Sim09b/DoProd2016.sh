#!/bin/bash

#2016
#from https://its.cern.ch/jira/browse/LHCBGAUSS-968
#Stripping 26

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4
Turbo=$5
muDST=$6

if [ "$Polarity" == "MagUp" ]; then
  SimCond=Gauss/Beam6500GeV-mu100-2016-nu1.6.py
  DBtag="sim-20161124-2-vc-mu100"
elif [ "$Polarity" == "MagDown" ]; then
  SimCond=Gauss/Beam6500GeV-md100-2016-nu1.6.py
  DBtag="sim-20161124-2-vc-md100"
else
  echo "Error, Polarity '$Polarity' is not valid!" 
  exit 1
fi

DDDBtag="dddb-20150724"

# Prepare conditions
echo "from Configurables import LHCbApp" >> Conditions.py
echo "LHCbApp().DDDBtag   = '$DDDBtag'" >> Conditions.py
echo "LHCbApp().CondDBtag = '$DBtag'" >> Conditions.py

#-------------# 
#   GAUSS     #
#-------------#

export CMTCONFIG=x86_64-slc6-gcc48-opt
source LbLogin.sh -c x86_64-slc6-gcc48-opt
source SetupProject.sh Gauss v49r5 --use "AppConfig v3r304"

# Prepare files
echo "from Gauss.Configuration import *" >> Gauss-Job.py
echo "GaussGen = GenInit('GaussGen')"    >> Gauss-Job.py
echo "GaussGen.FirstEventNumber = 1"     >> Gauss-Job.py
echo "GaussGen.RunNumber = $RunNumber"   >> Gauss-Job.py
echo "LHCbApp().EvtMax = $Nevents"       >> Gauss-Job.py


# Run
gaudirun.py $APPCONFIGOPTS/$SimCond $APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py $APPCONFIGOPTS/Gauss/DataType-2016.py $APPCONFIGOPTS/Gauss/RICHRandomHits.py $LBPYTHIA8ROOT/options/Pythia8.py $APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py $APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $Optfile Conditions.py Gauss-Job.py

# Prepare output
mv `ls *.sim` Gauss.sim
rm Gauss-Job.py

#-------------#
#   BOOLE     #
#-------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> Boole-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Gauss.sim' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Boole-Files.py
if [ "$Turbo" == "True" ]; then
  echo "from Configurables import Boole" >> Boole-Files.py
  echo "Boole().DigiType = 'Extended'" >> Boole-Files.py
  BooleOutput=Boole-Extended.digi
else
  BooleOutput=Boole.digi
fi

# Run
lb-run -c x86_64-slc6-gcc49-opt --use="AppConfig v3r304" Boole/v30r2 gaudirun.py \$APPCONFIGOPTS/Boole/Default.py \$APPCONFIGOPTS/Boole/EnableSpillover.py \$APPCONFIGOPTS/Boole/DataType-2015.py \$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Conditions.py Boole-Files.py

rm Gauss.sim
rm Boole-Files.py

#------------#
#     L0     #
#------------#

#Prepare special conditions
echo "from Gaudi.Configuration import *" > L0Configuration.py
echo "from Configurables import L0App" >> L0Configuration.py
echo 'L0App().outputFile="L0.digi"' >> L0Configuration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./$BooleOutput' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> L0Configuration.py

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r297" Moore/v25r4 gaudirun.py \$APPCONFIGOPTS/L0App/L0AppSimProduction.py \$APPCONFIGOPTS/L0App/L0AppTCK-0x160F.py \$APPCONFIGOPTS/L0App/ForceLUTVersionV8.py \$APPCONFIGOPTS/L0App/DataType-2016.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py L0Configuration.py

rm $BooleOutput
rm L0Configuration.py

#------------#
#    HLT1    #
#------------#

# Prepare special conditions
echo "from Gaudi.Configuration import *" > HLT1Configuration.py
echo "from Configurables import Moore" >> HLT1Configuration.py
echo "Moore().DDDBtag   = '$DDDBtag'" >> HLT1Configuration.py
echo "Moore().CondDBtag = '$DBtag'" >> HLT1Configuration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./L0.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> HLT1Configuration.py
echo "Moore().outputFile = 'HLT1.digi'" >> HLT1Configuration.py

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r297" Moore/v25r4 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x5138160F.py \$APPCONFIGOPTS/Moore/DataType-2016.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py \$APPCONFIGOPTS/Moore/MooreSimProductionHlt1.py HLT1Configuration.py

rm L0.digi
rm HLT1Configuration.py

#------------#
#    HLT2    #
#------------#

# Prepare special conditions
echo "from Gaudi.Configuration import *" > HLT2Configuration.py
echo "from Configurables import Moore" >> HLT2Configuration.py
echo "Moore().DDDBtag   = '$DDDBtag'" >> HLT2Configuration.py
echo "Moore().CondDBtag = '$DBtag'" >> HLT2Configuration.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./HLT1.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> HLT2Configuration.py
echo "Moore().outputFile = 'HLT2.digi'" >> HLT2Configuration.py

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r297" Moore/v25r4 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x6139160F.py \$APPCONFIGOPTS/Moore/DataType-2016.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py \$APPCONFIGOPTS/Moore/MooreSimProductionHlt2.py HLT2Configuration.py

rm HLT1.digi
rm HLT2Configuration.py

#-------------#
#   BRUNEL    #
#-------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> Brunel-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./HLT2.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Brunel-Files.py
if [ "$Turbo" == "True" ]; then
  echo "from Configurables import Brunel" >> Brunel-Files.py
  echo "Brunel().OutputType = 'XDST'" >> Brunel-Files.py
  BrunelOutput=Brunel.xdst
else
  BrunelOutput=Brunel.dst
fi

# Run
lb-run -c x86_64-slc6-gcc49-opt --use="AppConfig v3r314" --use="SQLDDDB v7r10" Brunel/v50r2 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2016.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Brunel/SplitRawEventOutput.4.3.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Brunel-Files.py Conditions.py

rm HLT2.digi
rm Brunel-Files.py

if [ "$Turbo" == "True" ]; then
  #-------------#
  #    TURBO    #
  #-------------#

  # Prepare files
  echo "from Gaudi.Configuration import *" >> Tesla-Files.py
  echo "EventSelector().Input = [\"DATAFILE='PFN:./$BrunelOutput' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Tesla-Files.py
  if [ "$muDST" == "True" ]; then
    echo 'importOptions("$APPCONFIGOPTS/Turbo/Tesla_FilterMC.py")' >> Tesla-Files.py
  fi  

  #run
  lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r322" --use="TurboStreamProd v4r1p4" DaVinci/v41r2p5 gaudirun.py \$APPCONFIGOPTS/Turbo/Tesla_2016_LinesFromStreams_MC.py \$APPCONFIGOPTS/Turbo/Tesla_PR_Truth_2016.py \$APPCONFIGOPTS/Turbo/Tesla_Simulation_2016.py Conditions.py Tesla-Files.py

  rm $BrunelOutput
  rm Tesla-Files.py
  
  TurboOutput=Tesla.dst	
else
  TurboOutput=$BrunelOutput
fi

#------------------------#
#   DAVINCI/STRIPPING    #
#------------------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> DaVinci-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./$TurboOutput' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> DaVinci-Files.py
if [ "$muDST" == "True" ]; then
  echo 'importOptions("$APPCONFIGOPTS/DaVinci/DV-Stripping-MC-muDST.py")' >> DaVinci-Files.py
fi

## Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r322" DaVinci/v41r2p5 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping26-Stripping-MC-NoPrescaling-DST.py \$APPCONFIGOPTS/DaVinci/DataType-2016.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py Conditions.py DaVinci-Files.py

rm $TurboOutput
rm DaVinci-Files.py

rm *.root
rm *.py

rm test_catalog.xml
rm NewCatalog.xml

if [ "$muDST" == "True" ]; then
  mv *AllStreams.mdst ${Nevents}_events.mdst
else
  mv *AllStreams.dst ${Nevents}_events.dst
fi

# Finish

# EOF