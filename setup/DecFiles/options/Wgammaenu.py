# Pythia options for Wgamma->enu 42511102
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 0" ,       # Turn off general production
    "pysubs msub 20 1",     # Turn on Wgamma
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
    "pydat3 mdme 206 1 1", #Turn on W->enue
    "pydat3 mdme 207 1 0",
    "pydat3 mdme 208 1 0",
    "pydat3 mdme 209 1 0"
]

Generation().Special.Pythia8Production.Commands += [
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "WeakBosonAndParton:ffbar2Wgm  = on", #f f -> W gamma
    "24:onMode = off", #Turn off W decays
    "24:onIfAny = 11 -11" #Turn on e+/e- decay
    ]
