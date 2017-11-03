# Pythia options for qqbar -> t tbar
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
        "pysubs msub 82 0" , #turn gg->Q Qbar off
        "pysubs msub 81 1" , #turn qqbar->Q Qbar on
        "pypars mstp 7 6" #select top = 6 flavour
        ]

#pythia 8 production commands
Generation().Special.Pythia8Production.Commands += [
    "TimeShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTmaxMatch = 0", #Kinematic limit
    "SpaceShower:pTdampMatch = 1", #Apply damping
    "TimeShower:pTdampMatch = 1", #Apply damping
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "SpaceShower:phiIntAsym = off", #Pythia asymmetric showering bug
    "Top:qqbar2ttbar = on", #seperate gg and qqbar processes for scaling
]
