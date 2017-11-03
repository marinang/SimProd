from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 0" ,
    "pysubs msub 82 1" ,
    "pysubs msub 81 1" ,
    "pypars mstp 7 6"
]
