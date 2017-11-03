# Pythia options for Z->cc+jet 42900012
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [ 
                "SpaceShower:rapidityOrder = off", #pT ordering!
                "WeakBosonAndParton:qg2gmZq = on", #q g -> Z q
                "WeakBosonAndParton:qqbar2gmZg = on", #q qbar -> Z g
                "23:onMode = off", #Turn Z decays off
                "23:onIfAny = 4" #Turn on decay to c quarks
                 ]
