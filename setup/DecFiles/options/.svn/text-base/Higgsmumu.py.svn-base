# Pythia options for Higgsmumu
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
            "HiggsSM:all = on",  #Switch H_25 (H) production on
            "25:onMode = off", #Turn W decay off
            "25:onIfAny = 13", #Turn on mu+, mu- decays
            "PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
            #Change of H_25 (H) mass is done in the dkfile
        ]
