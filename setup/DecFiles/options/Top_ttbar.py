# Pythia options for t tbar
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

#pythia 8 production commands
Generation().Special.Pythia8Production.Commands += [
    "TimeShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTdampMatch = 1", #Apply damping
    "TimeShower:pTdampMatch = 1", #Apply damping
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "SpaceShower:phiIntAsym = off", #Pythia asymmetric showering bug
    "Top:qqbar2ttbar = on", 
    "Top:gg2ttbar = on"
]
