from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions("$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py")

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

#Pythia8 configuration
Generation().Special.Pythia8Production.Commands += [
             "PhaseSpace:pTHatMin = 20.",
             "LeftRightSymmmetry:ffbar2WR = on",
             "9900014:oneChannel = 1 1 0 13 -1 2",
             "9900014:doForceWidth = 1",
             "9900014:isResonance = true",
             "9900024:onMode = off",
             "9900024:oneChannel = 1 1 0 -13 9900014"
        ]

from Configurables import GenerationToSimulation
GenerationToSimulation("GenToSim").KeepCode = "in_list( GABSID, [ 'nu_Rmu', 'W_R-' ] ) & ( GSTATUS == LHCb.HepMCEvent.DocumentationParticle )"
