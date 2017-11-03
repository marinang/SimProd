# Pythia options for A1mumu
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
            "Higgs:useBSM = on", #Switch Higgs BSM on
            "HiggsBSM:allA3 = on", #Switch H_30 (A0) production on
            "36:onMode = off", #Turn W decay off
            "36:onIfAny = 13", #Turn on mu+, mu- decays
            "PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
            #Change of H_30 (A0) mass is done in the dkfile
        ]
