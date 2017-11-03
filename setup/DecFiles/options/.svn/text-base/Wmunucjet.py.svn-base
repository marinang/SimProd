# Pythia options for W->munucjet 42971000
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msub 31 1" ,

    "pysubs kfin 1 1 0",
    "pysubs kfin 1 2 0",
    "pysubs kfin 1 3 1", 
    "pysubs kfin 1 4 0",
    "pysubs kfin 1 5 0",
    "pysubs kfin 1 6 0",

    "pysubs kfin 1 -1 0",
    "pysubs kfin 1 -2 0",
    "pysubs kfin 1 -3 1", 
    "pysubs kfin 1 -4 0",
    "pysubs kfin 1 -5 0",
    "pysubs kfin 1 -6 0",

    "pysubs kfin 2 1 0",
    "pysubs kfin 2 2 0",
    "pysubs kfin 2 3 1", 
    "pysubs kfin 2 4 0",
    "pysubs kfin 2 5 0",
    "pysubs kfin 2 6 0",

    "pysubs kfin 2 -1 0",
    "pysubs kfin 2 -2 0",
    "pysubs kfin 2 -3 1", 
    "pysubs kfin 2 -4 0",
    "pysubs kfin 2 -5 0",
    "pysubs kfin 2 -6 0",

    "pydat2 vckm 1 1 1",
    "pydat2 vckm 1 2 0",
    "pydat2 vckm 1 3 0",
    "pydat2 vckm 1 4 0",
    "pydat2 vckm 2 1 0",
    "pydat2 vckm 2 2 1",
    "pydat2 vckm 2 3 0",
    "pydat2 vckm 2 4 0",
    "pydat2 vckm 3 1 0",
    "pydat2 vckm 3 2 0",
    "pydat2 vckm 3 3 1",
    "pydat2 vckm 3 4 0",
    "pydat2 vckm 4 1 0",
    "pydat2 vckm 4 2 0",
    "pydat2 vckm 4 3 0",
    "pydat2 vckm 4 4 1",

    "pydat3 mdme 190 1 0" ,
    "pydat3 mdme 191 1 0" ,
    "pydat3 mdme 192 1 0" ,
    "pydat3 mdme 193 1 0" ,
    "pydat3 mdme 194 1 0" ,
    "pydat3 mdme 195 1 0" ,
    "pydat3 mdme 196 1 0" ,
    "pydat3 mdme 197 1 0" ,
    "pydat3 mdme 198 1 0" ,
    "pydat3 mdme 199 1 0" ,
    "pydat3 mdme 200 1 0" ,
    "pydat3 mdme 201 1 0" ,
    "pydat3 mdme 202 1 0" ,
    "pydat3 mdme 203 1 0" ,
    "pydat3 mdme 204 1 0" ,
    "pydat3 mdme 205 1 0",
    "pydat3 mdme 206 1 0",
    "pydat3 mdme 207 1 1",
    "pydat3 mdme 208 1 0",
    "pydat3 mdme 209 1 0"
#    "pyinit pyliste 1"
]

