# Pythia8 options for WZ->lnu +ll 1 lepton only 42923002
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )


#pythia 8 production commands
Generation().Special.Pythia8Production.Commands += [
    "TimeShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTdampMatch = 1", #Apply damping
    "TimeShower:pTdampMatch = 1", #Apply damping
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "SpaceShower:phiIntAsym = off", #Pythia asymmetric showering bug
    "WeakDoubleBoson:ffbar2ZW = on",
    "24:onMode = off",
    "24:onIfAny = 11 -11",
    "24:onIfAny = 13 -13",
    "23:onMode = off",
    "23:onIfAny = 11",
    "23:onIfAny = 13"
    #"PartonLevel:FSR = on", # final state radiation
    #"PartonLevel:ISR = on", # initial state radiation
    #"PartonLevel:MI = off", # multiple interactions
]
