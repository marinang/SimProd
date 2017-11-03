# Pythia options for inclusive W
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

#pythia8 production commands
Generation().Special.Pythia8Production.Commands += [
            "SpaceShower:rapidityOrder = off", #pT ordering!
            "WeakSingleBoson:ffbar2W = on" 
            "WeakDoubleBoson:ffbar2ZW = on"
            "WeakDoubleBoson:ffbar2WW = on"
            "WeakBosonAndParton:qqbar2Wg = on", #q qbar -> W g
            "WeakBosonAndParton:qg2Wq = on", #q g -> W q
        ]
