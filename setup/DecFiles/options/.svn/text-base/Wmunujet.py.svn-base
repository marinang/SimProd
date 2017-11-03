# Pythia options for W->munujet 42311010
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )
#Pythia 6 production commands
Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 14" ,
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
]
#pythia8 production commands
Generation().Special.Pythia8Production.Commands += [
            "SpaceShower:rapidityOrder = off", #pT ordering!
            "WeakBosonAndParton:qqbar2Wg = on", #q qbar -> W g
            "WeakBosonAndParton:qg2Wq = on", #q g -> W q
            "24:onMode = off", #Turn W decay off
            "24:onIfAny = 13 -13" #Turn on mu+, mu- decays
        ]
