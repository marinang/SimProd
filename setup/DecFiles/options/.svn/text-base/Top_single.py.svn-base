# Pythia options for single top
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

#pythia 6 commands - Needs fix since selecting only top heavy flavour ruins top decay to b
#Generation().Special.PythiaProduction.Commands += [
#        "pysubs msel 0" ,
#        "pysubs msub 83 1" ,
#        "pypars mstp 7 6"
#        ]

#pythia 8 production commands
Generation().Special.Pythia8Production.Commands += [
    "TimeShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTdampMatch = 1", #Apply damping
    "TimeShower:pTdampMatch = 1", #Apply damping
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "SpaceShower:phiIntAsym = off", #Pythia asymmetric showering bug
    "Top:qq2tq(t:W) = on", #single top (t-channel)
    "Top:ffbar2tqbar(s:W) = on", #single top (s-channel)
]
