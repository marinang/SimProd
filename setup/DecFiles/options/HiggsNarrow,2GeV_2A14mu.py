# Pythia options for HiggsNarrow,2GeV_2A14mu
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
            "Higgs:useBSM = on",
            "HiggsBSM:allH2 = on",
                      
            "35:mWidth = 6.40e-05", #width in GeV
            "35:m0 = 2.0", #mass in GeV
            "35:doForceWidth = true",
            "35:doExternalDecay = true",
                     
            "PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
            #Change of all masses and lifetimes mass is done in the dkfile
        ]
