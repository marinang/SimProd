# Pythia options for gg->tt
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

#pythia 6 commands
Generation().Special.PythiaProduction.Commands += [
        "pysubs msel 0" ,
        "pysubs msub 82 1" , #turn gg->Q Qbar on
        "pysubs msub 81 0" , #turn qqbar->Q Qbar off
        "pypars mstp 7 6" #select flavour of Q = top
        ]

#pythia 8 production commands
Generation().Special.Pythia8Production.Commands += [
    "TimeShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTdampMatch = 1", #Apply damping
    "TimeShower:pTdampMatch = 1", #Apply damping
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "SpaceShower:phiIntAsym = off", #Pythia asymmetric showering bug
    "Top:gg2ttbar = on", #seperate gg and qqbar processes for scaling
]
