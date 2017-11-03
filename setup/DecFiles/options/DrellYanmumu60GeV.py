# Pythia options for DYmumu at 60 GeV (Pythia 8)
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

#pythia8 production commands
Generation().Special.Pythia8Production.Commands += ["WeakSingleBoson:ffbar2gmZ = on",
                                                    "23:onMode = off", # turn off all decays modes
                                                    "23:onIfAny = 13", # turn on the mu+mu- decay mode
                                                    "PhaseSpace:mHatMin = 60."] # lower invariant mass

