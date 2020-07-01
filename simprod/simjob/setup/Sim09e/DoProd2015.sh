#!/bin/bash

#from https://its.cern.ch/jira/browse/LHCBGAUSS-1184
#Stripping 24r1/24r1p1

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
	SimCond=Gauss/Beam6500GeV-mu100-2015-nu1.6.py
	DBtag="sim-20161124-vc-mu100"
elif [ "$Polarity" == "MagDown" ]; then
	SimCond=Gauss/Beam6500GeV-md100-2015-nu1.6.py
	DBtag="sim-20161124-vc-md100"
else
	echo "Error, Polarity '$3' is not valid!" 
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

if [ "$Model" == "pythia8" ]; then
	model=LBPYTHIA8ROOT/options/Pythia8.py
elif [ "$Model" == "BcVegPy" ]; then
	model=LBBCVEGPYROOT/options/BcVegPyPythia8.py
fi

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
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r359" Gauss/v49r11 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py \$APPCONFIGOPTS/Gauss/DataType-2015.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py \$APPCONFIGOPTS/Gauss/ReDecay-100times.py \$APPCONFIGOPTS/Gauss/ReDecay-FullGenEventCutTool-fix.py $Optfile $CONDITIONS $GAUSSJOB
else
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r335" Gauss/v49r11 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py \$APPCONFIGOPTS/Gauss/DataType-2015.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $Optfile $CONDITIONS $GAUSSJOB
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
lb-run -c x86_64-slc6-gcc49-opt --use "AppConfig v3r338" Boole/v30r2p1 gaudirun.py \$APPCONFIGOPTS/Boole/Default.py \$APPCONFIGOPTS/Boole/EnableSpillover.py \$APPCONFIGOPTS/Boole/DataType-2015.py \$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $CONDITIONS $BOOLEFILES

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
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r268" Moore/v24r2 gaudirun.py \$APPCONFIGOPTS/L0App/L0AppSimProduction.py \$APPCONFIGOPTS/L0App/L0AppTCK-0x00a2.py \$APPCONFIGOPTS/L0App/ForceLUTVersionV8.py \$APPCONFIGOPTS/L0App/DataType-2015.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $L0CONFIG $CONDITIONS

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
echo "EventSelector().Input = [\"DATAFILE='PFN:$L0OUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $MOORECONFIG
echo "Moore().outputFile = '$MOOREOUTPUT'" >> $MOORECONFIG

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r268" Moore/v24r2 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x411400a2.py \$APPCONFIGOPTS/Moore/DataType-2015.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $MOORECONFIG $CONDITIONS

rm $L0OUTPUT
rm $MOORECONFIG

#-------------#
#   BRUNEL    #
#-------------#

BRUNELFILES=$PWD/Brunel-Files.py

# Prepare files
echo "from Gaudi.Configuration import *" >> $BRUNELFILES
echo "EventSelector().Input = [\"DATAFILE='PFN:$MOOREOUTPUT' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> $BRUNELFILES
if [ "$Turbo" == "True" ]; then
	echo "from Configurables import Brunel" >> $BRUNELFILES
	echo "Brunel().OutputType = 'XDST'" >> $BRUNELFILES
	BRUNELOUTPUT=$PWD/Brunel.xdst
else
	BRUNELOUTPUT=$PWD/Brunel.dst
fi

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r277" --use="SQLDDDB v7r10" Brunel/v48r2p1 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2015.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $BRUNELFILES $CONDITIONS

rm $MOOREOUTPUT
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
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r232" --use="TurboStreamProd v2r0" DaVinci/v40r1p3 gaudirun.py \$APPCONFIGOPTS/Turbo/Tesla_AllHlt2Lines_v10r0_0x00fa0051.py \$APPCONFIGOPTS/Turbo/Tesla_Simulation_2015_PVHLT2.py $CONDITIONS $TESLAFILES
	
	rm $BRUNELOUTPUT
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
	echo 'importOptions("$APPCONFIGOPTS/DaVinci/DV-Stripping-MC-muDST.py")'	>> $DAVINCIFILES
fi

if [ "$Stripping" == "24r1" ]; then
	lb-run -c x86_64-slc6-gcc49-opt --use="AppConfig v3r343" DaVinci/v38r1p6 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping24r1-Stripping-MC-NoPrescaling-DST.py \$APPCONFIGOPTS/DaVinci/DataType-2015.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py $CONDITIONS $DAVINCIFILES
elif [ "$Stripping" == "24r1p1" ]; then
	lb-run -c x86_64-slc6-gcc49-opt --use="AppConfig v3r343" DaVinci/v38r1p7 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping24r1p1-Stripping-MC-NoPrescaling-DST.py \$APPCONFIGOPTS/DaVinci/DataType-2015.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py $CONDITIONS $DAVINCIFILES
fi

# Run

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


