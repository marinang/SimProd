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
            #"HiggsSM:gg2H = on", #Switch gg H_25 (H) production on
            "HiggsSM:ff2Hff(t:ZZ)  = on",
            "HiggsSM:ff2Hff(t:WW)  = on",
            "25:onMode = off", #Turn H decays off
            "25:onIfAny = 5", #Turn on bbar decays
            "PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
            #Change of H_25 (H) mass is done in the dkfile
        ]
