# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/49000154.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 49000154
#
# ASCII decay Descriptor: pp -> (tau + tau) ...
#
from Configurables import Generation
Generation().EventType = 49000154
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ditau=gamma,m90GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 2
Generation().Special.PythiaHiggsType.LeptonPtMin = 0
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
Generation().Special.PythiaHiggsType.MotherOfLepton = ["Z0"]
Generation().Special.PythiaHiggsType.TypeOfLepton = ["tau+"]

# Switch off all Pythia 6 and Pythia 8 options.
from Gaudi.Configuration import importOptions
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

# Pythia 8 options.
from Configurables import Pythia8Production
Generation().Special.addTool( Pythia8Production )
Generation().Special.Pythia8Production.Commands += [
    "WeakZ0:gmZmode = 1",             # Only gamma contribution.
    "WeakSingleBoson:ffbar2gmZ = on", # Hard process.
    "PhaseSpace:mHatMin = 90.0",      # Minimum mass.
    "23:mMin = 5.0",                  # Minimum Z mass.
    "23:onMode = off",                # Turn off all Z decays.
    "23:onIfMatch = -15 15"]          # Turn on ditau channel.

# Turn off EvtGen.
Generation().DecayTool = ""
Generation().Special.DecayTool = ""

# Keep Z in MCParticles.
from Configurables import GenerationToSimulation
GenerationToSimulation("GenToSim").KeepCode = "GABSID == 'Z0'"

