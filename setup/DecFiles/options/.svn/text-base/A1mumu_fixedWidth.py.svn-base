# Pythia options for A1mumu_fixedWidth
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

# Pythia8 production commands
Generation().Special.Pythia8Production.Commands += [
                                                    "SpaceShower:rapidityOrder = off" # pT ordering
                                                    ,"Higgs:useBSM = on" # Switch Higgs BSM on
                                                    ,"HiggsBSM:allA3 = on" # Switch H_30 (A0) production on
                                                    ,"36:onMode = off" # Turn off all decays for A0
                                                    ,"36:onIfAny = 13" # Turn on only A0->mumu decay
                                                    ,"PartonLevel:FSR=on" # FSR by PYTHIA8 (NOT PHOTOS)
                                                    ,"36:doForceWidth = on" # Fix maximum width to avoid problems with 2->1 processes 
                                                    ]
