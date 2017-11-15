#!/bin/bash

#from https://its.cern.ch/jira/browse/LHCBGAUSS-1184
#Stripping 24r0p1

# 1 = EvtType
# 2 = nbr of evts
# 3 = Polarity
# 4 = muDST

Optfile=$1
Nevents=$2
Polarity=$3
RunNumber=$4
Turbo=$5
muDST=$6

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
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r335" Gauss/v49r8 gaudirun.py \$APPCONFIGOPTS/$SimCond \$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py \$APPCONFIGOPTS/Gauss/DataType-2015.py \$APPCONFIGOPTS/Gauss/RICHRandomHits.py \$LBPYTHIA8ROOT/options/Pythia8.py \$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py $Optfile Conditions.py Gauss-Job.py

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
lb-run -c x86_64-slc6-gcc49-opt --use "AppConfig v3r338" Boole/v30r2p1 gaudirun.py \$APPCONFIGOPTS/Boole/Default.py \$APPCONFIGOPTS/Boole/EnableSpillover.py \$APPCONFIGOPTS/Boole/DataType-2015.py \$APPCONFIGOPTS/Boole/Boole-SetOdinRndTrigger.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Conditions.py Boole-Files.py

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
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r268" Moore/v24r2 gaudirun.py \$APPCONFIGOPTS/L0App/L0AppSimProduction.py \$APPCONFIGOPTS/L0App/L0AppTCK-0x00a2.py \$APPCONFIGOPTS/L0App/ForceLUTVersionV8.py \$APPCONFIGOPTS/L0App/DataType-2015.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py L0Configuration.py Conditions.py

rm $BooleOutput
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
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r268" Moore/v24r2 gaudirun.py \$APPCONFIGOPTS/Moore/MooreSimProductionForSeparateL0AppStep2015.py \$APPCONFIGOPTS/Conditions/TCK-0x411400a2.py \$APPCONFIGOPTS/Moore/DataType-2015.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py MooreConfiguration.py Conditions.py

#-------------#
#   BRUNEL    #
#-------------#

# Prepare files
echo "from Gaudi.Configuration import *" >> Brunel-Files.py
echo "EventSelector().Input = [\"DATAFILE='PFN:./Moore.digi' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Brunel-Files.py
if [ "$Turbo" == "True" ]; then
	echo "from Configurables import Brunel" >> Brunel-Files.py
	echo "Brunel().OutputType = 'XDST'" >> Brunel-Files.py
	BrunelOutput=Brunel.xdst
else
	BrunelOutput=Brunel.dst
fi

# Run
lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r277" --use="SQLDDDB v7r10" Brunel/v48r2p1 gaudirun.py \$APPCONFIGOPTS/Brunel/DataType-2015.py \$APPCONFIGOPTS/Brunel/MC-WithTruth.py \$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py Brunel-Files.py Conditions.py

rm Moore.digi
rm Brunel-Files.py

if [ "$Turbo" == "True" ]; then
	#-------------#
	#    TURBO    #
	#-------------#

	# Prepare files
	echo "from Gaudi.Configuration import *" >> Tesla-Files.py
	echo "EventSelector().Input = [\"DATAFILE='PFN:./$BrunelOutput' TYP='POOL_ROOTTREE' OPT='READ'\"]" >> Tesla-Files.py

	#run
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r232" --use="TurboStreamProd v2r0" DaVinci/v40r1p3 gaudirun.py \$APPCONFIGOPTS/Turbo/Tesla_AllHlt2Lines_v10r0_0x00fa0051.py \$APPCONFIGOPTS/Turbo/Tesla_Simulation_2015_PVHLT2.py Conditions.py Tesla-Files.py
	
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
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r227" DaVinci/v38r1p1 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping24-Stripping-MC-NoPrescaling.py \$APPCONFIGOPTS/DaVinci/DV-Stripping-MC-muDST.py \$APPCONFIGOPTS/DaVinci/DataType-2015.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py Conditions.py DaVinci-Files.py
else
	lb-run -c x86_64-slc6-gcc48-opt --use="AppConfig v3r338" DaVinci/v38r1p1 gaudirun.py \$APPCONFIGOPTS/DaVinci/DV-Stripping24-Stripping-MC-NoPrescaling-DST.py \$APPCONFIGOPTS/DaVinci/DataType-2015.py \$APPCONFIGOPTS/DaVinci/InputType-DST.py Conditions.py DaVinci-Files.py

# Run

rm $TurboOutput
rm DaVinci-Files.py

rm *.root
rm *.py

rm test_catalog.xml
rm NewCatalog.xml

mv *AllStreams.dst ${Nevents}_events.dst

# Finish

# EOF


