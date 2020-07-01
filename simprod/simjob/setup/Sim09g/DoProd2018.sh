#!/bin/bash

#2018
#from https://its.cern.ch/jira/browse/LHCBGAUSS-1190
#Stripping 34, 34r0p1

. /cvmfs/lhcb.cern.ch/lib/LbEnv

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4
Turbo=$5
muDST=$6
Stripping=$7
ReDecay=$8
Model=${9:-"pythia8"}

if [ "$Polarity" == "MagUp" ]; then
	SimCond=Gauss/Beam6500GeV-mu100-2018-nu1.6.py
	DBtag="sim-20190430-vc-mu100"
elif [ "$Polarity" == "MagDown" ]; then
	SimCond=Gauss/Beam6500GeV-md100-2018-nu1.6.py
	DBtag="sim-20190430-vc-md100"
else
	echo "Error, Polarity '$Polarity' is not valid!" 
	exit 1
fi

DDDBtag="dddb-20170721-3"

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

if [ "$Model" == "pythia8" ]; then
	echo 'importOptions("$LBPYTHIA8ROOT/options/Pythia8.py")' >> $GAUSSJOB
elif [ "$Model" == "BcVegPy" ]; then
	echo 'importOptions("$LBBCVEGPYROOT/options/BcVegPyPythia8.py")' >> $GAUSSJOB
else
	echo 'importOptions("$LBPYTHIA8ROOT/options/Pythia8.py")' >> $GAUSSJOB
fi

echo "from Configurables import OutputStream" >> $GAUSSJOB
echo "OutputStream('GaussTape').Output = \"DATAFILE='PFN:$GAUSSOUTPUT' TYP='POOL_ROOTTREE' OPT='RECREATE'\"" >> $GAUSSJOB


# Run
if [ "$ReDecay" == "True" ]; then
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r375" Gauss/v49r13 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py \$APPCONFIGOPTS/Gauss/DataType-2017.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py \$APPCONFIGOPTS/Gauss/ReDecay-100times.py \$APPCONFIGOPTS/Gauss/ReDecay-FullGenEventCutTool-fix.py $Optfile $CONDITIONS $GAUSSJOB
else
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r375" Gauss/v49r13 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py \$APPCONFIGOPTS/Gauss/DataType-2017.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $Optfile $CONDITIONS $GAUSSJOB
fi

rm $GAUSSJOB

#-------------#
#   BOOLE     #
#-------------#

BOOLEFILES=$PWD/Boole-Files.py

# Prepare files
echo "from Gaudi.Configuration import *" >> $BOOLEFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$GAUSSOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $BOOLEFILES
if [ "$Turbo" == "True" ]; then
	echo "from Configurables import Boole" >> $BOOLEFILES
	echo "Boole().DigiType = 'Extended'" >> $BOOLEFILES
	BOOLEOUTPUT=$PWD/Boole-Extended.digi
else
	BOOLEOUTPUT=$PWD/Boole.digi
fi
	
# Run
lb-run -c x86_64-slc6-gcc49-opt --use="AppConfig v3r374" Boole/v30r4 gaudirun.py \$APPCONFIGOPTS/Boole/Default.py \$APPCONFIGOPTS/Boole/EnableSpillover.py \$APPCONFIGOPTS/Boole/DataType-2015.py \$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py $CONDITIONS $BOOLEFILES

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
lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r374" Moore/v28r3p1 gaudirun.py \$APPCONFIGOPTS/L0App/L0AppSimProduction.py \$APPCONFIGOPTS/L0App/L0AppTCK-0x18a4.py \$APPCONFIGOPTS/L0App/ForceLUTVersionV8.py \$APPCONFIGOPTS/L0App/DataType-2017.py $L0CONFIG $CONDITIONS

rm $BOOLEOUTPUT
rm $L0CONFIG

#------------#
#    HLT1    #
#------------#

HLT1CONFIG=$PWD/HLT1Configuration.py
HLT1OUTPUT=$PWD/HLT1.digi

# Prepare special conditions
echo "from Gaudi.Configuration import *" > $HLT1CONFIG
echo "from Configurables import Moore" >> $HLT1CONFIG
echo "Moore().DDDBtag   = '$DDDBtag'" >> $HLT1CONFIG
echo "Moore().CondDBtag = '$DBtag'" >> $HLT1CONFIG
echo "EventSelector().Input = [\"DATAFILE='PFN:$L0OUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $HLT1CONFIG
echo "Moore().outputFile = '$HLT1OUTPUT'" >> $HLT1CONFIG

# Run
lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r374" Moore/v28r3p1 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x517a18a4.py \$APPCONFIGOPTS/Moore/DataType-2017.py \$APPCONFIGOPTS/Moore/MooreSimProductionHlt1.py $HLT1CONFIG $CONDITIONS

rm $L0OUTPUT
rm $HLT1CONFIG

#------------#
#    HLT2    #
#------------#

HLT2CONFIG=$PWD/HLT2Configuration.py
HLT2OUTPUT=$PWD/HLT2.digi

# Prepare special conditions
echo "from Gaudi.Configuration import *" > $HLT2CONFIG
echo "from Configurables import Moore" >> $HLT2CONFIG
echo "Moore().DDDBtag   = '$DDDBtag'" >> $HLT2CONFIG
echo "Moore().CondDBtag = '$DBtag'" >> $HLT2CONFIG
echo "EventSelector().Input = [\"DATAFILE='PFN:$HLT1OUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $HLT2CONFIG
echo "Moore().outputFile = '$HLT2OUTPUT'" >> $HLT2CONFIG

# Run
lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r374" Moore/v28r3p1 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x617d18a4.py \$APPCONFIGOPTS/Moore/DataType-2017.py \$APPCONFIGOPTS/Moore/MooreSimProductionHlt2.py $HLT2CONFIG $CONDITIONS

rm $HLT1OUTPUT
rm $HLT2CONFIG

#-------------#
#   BRUNEL    #
#-------------#

BRUNELFILES=$PWD/Brunel-Files.py

# Prepare files
echo "from Gaudi.Configuration import *" >> $BRUNELFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$HLT2OUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $BRUNELFILES
if [ "$Turbo" == "True" ]; then
	echo "from Configurables import Brunel" >> $BRUNELFILES
	echo "Brunel().OutputType = 'XDST'" >> $BRUNELFILES
	BRUNELOUTPUT=$PWD/Brunel.xdst
else
	BRUNELOUTPUT=$PWD/Brunel.dst
fi

# Run
lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r374" --use="SQLDDDB v7r10" Brunel/v54r2 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2018.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Brunel/SplitRawEventOutput.4.3.py $BRUNELFILES $CONDITIONS

rm $HLT2OUTPUT
rm $BRUNELFILES

if [ "$Turbo" == "True" ]; then
	#-------------#
	#    TURBO    #
	#-------------#
	
	TESLAFILES=$PWD/Tesla-Files.py

	# Prepare files
	echo "from Gaudi.Configuration import *" >> $TESLAFILES
	echo "EventSelector().Input = [\"DATAFILE='PFN:$BRUNELOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $TESLAFILES
	if [ "$muDST" == "True" ]; then
		echo 'importOptions("$APPCONFIGOPTS/Turbo/Tesla_FilterMC.py")' >> $TESLAFILES
	fi  
		
	#run
	lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r374" --use="TurboStreamProd v4r2p10" DaVinci/v44r7 gaudirun.py \$APPCONFIGOPTS/Turbo/Tesla_2018_LinesFromStreamsAndTurCal_MC.py \$APPCONFIGOPTS/Turbo/Tesla_Simulation_2018.py $CONDITIONS $TESLAFILES 

	rm $BrunelOutput
	rm $TESLAFILES
	
	TURBOOUTPUT=$PWD/Tesla.dst	
else
	TURBOOUTPUT=$BRUNELOUTPUT
fi

#------------------------#
#   DAVINCI/STRIPPING    #
#------------------------#

DAVINCIFILES=$PWD/DaVinci-Files.py

# Prepare files
echo "from Gaudi.Configuration import *" >> $DAVINCIFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$TURBOOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $DAVINCIFILES
if [ "$muDST" == "True" ]; then
	echo 'importOptions("$APPCONFIGOPTS/DaVinci/DV-Stripping-MC-muDST.py")' >> $DAVINCIFILES
fi

## Run

## Run
if [ "$Stripping" == "34" ]; then
	lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r376" --use="TMVAWeights v1r10" DaVinci/v44r7 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping34-Stripping-MC-NoPrescaling-DST.py \$APPCONFIGOPTS/DaVinci/DataType-2018.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py $CONDITIONS $DAVINCIFILES
elif [ "$Stripping" == "34r0p1" ]; then
	lb-run -c x86_64-slc6-gcc62-opt --use="AppConfig v3r376" --use="TMVAWeights v1r11" DaVinci/v44r10p2 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping34r0p1-Stripping-MC-NoPrescaling-DST.py \$APPCONFIGOPTS/DaVinci/DataType-2018.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py $CONDITIONS $DAVINCIFILES
fi



rm $TURBOOUTPUT
rm $DAVINCIFILES

rm *.root
rm *.py
rm core.*

rm test_catalog.xml
rm NewCatalog.xml

if [ "$muDST" == "True" ]; then
	mv *AllStreams.mdst ${PWD}/${Nevents}_events.mdst
else
	mv *AllStreams.dst ${PWD}/${Nevents}_events.dst
fi

# Finish

# EOF
