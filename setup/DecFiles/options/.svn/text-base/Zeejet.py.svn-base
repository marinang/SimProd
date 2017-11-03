# Pythia options for Z->eejet 42122020
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [  "pysubs msel 13" ,
                                                     "pypars mstp 43 2" ,
                                                     "pydat3 mdme 174 1 0" ,
                                                     "pydat3 mdme 175 1 0" ,
                                                     "pydat3 mdme 176 1 0" ,
                                                     "pydat3 mdme 177 1 0" ,
                                                     "pydat3 mdme 178 1 0" ,
                                                     "pydat3 mdme 179 1 0" ,
                                                     "pydat3 mdme 180 1 0" ,
                                                     "pydat3 mdme 181 1 0" ,
                                                     "pydat3 mdme 182 1 1" ,
                                                     "pydat3 mdme 183 1 0" ,
                                                     "pydat3 mdme 184 1 0" ,
                                                     "pydat3 mdme 185 1 0" ,
                                                     "pydat3 mdme 186 1 0" ,
                                                     "pydat3 mdme 187 1 0" ,
                                                     "pydat3 mdme 188 1 0" ,
                                                     "pydat3 mdme 189 1 0"
                                                     ] 

Generation().Special.Pythia8Production.Commands += [
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "WeakBosonAndParton:qqbar2gmZg = on", #q qbar -> gamma^*/Z^0 g
    "WeakBosonAndParton:qg2gmZq = on", #q g -> gamma^*/Z^0 q
    "WeakZ0:gmZmode = 2", #Z0 only
    "23:onMode = off", #turn it off
    "23:onIfMatch = 11 -11" # turn it on for the decay to e final state only
    ]
