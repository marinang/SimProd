# Pythia options for Zgamma->ee 42112102
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [ "pysubs msel 0" ,       # Turn off general production
                                                    "pypars mstp 43 2" ,    # Only consider Z0 (no gamma*)
                                                    "pysubs msub 19 1" ,    # Turn on Z0gamma
                                                    "pydat3 mdme 174 1 0" , 
                                                    "pydat3 mdme 175 1 0" ,
                                                    "pydat3 mdme 176 1 0" ,
                                                    "pydat3 mdme 177 1 0" ,
                                                    "pydat3 mdme 178 1 0" ,
                                                    "pydat3 mdme 179 1 0" ,
                                                    "pydat3 mdme 180 1 0" ,
                                                    "pydat3 mdme 181 1 0" ,
                                                    "pydat3 mdme 182 1 1" , #Z->ee
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
  "WeakBosonAndParton:ffbar2gmZgm = on", #f f -> Z gamma
  "WeakZ0:gmZmode = 2",
  "23:onMode = off", #Turn off Z decays
  "23:onIfAny = -11 11" #Turn on e+ e- decay
  ]
