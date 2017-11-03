# Pythia options for hard scatter production with pthat>20GeV
from Configurables import Generation
from Gaudi.Configuration import *
Generation().PileUpTool = "FixedLuminosityForRareProcess";

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msub 11 1" ,
    "pysubs msub 12 1" ,
    "pysubs msub 13 1" ,
    "pysubs msub 28 1" ,
    "pysubs msub 53 1" ,
    "pysubs msub 68 1" ,
    "pysubs ckin 3 20",
    "pysubs ckin 4 -1",
    ]



