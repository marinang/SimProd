# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42102220.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 42102220
#
# ASCII decay Descriptor: pp -> [Z -> (phi(1020) -> K+ K-) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42102220
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_Phigamma=NoCut.dec"
Generation().Special.CutTool = ""

Generation().PileUpTool = "FixedLuminosityForRareProcess"

# Pythia8 options.
from Gaudi.Configuration import importOptions
from Configurables import Pythia8Production
importOptions('$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py')
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    'WeakSingleBoson:ffbar2gmZ = on',
    'WeakZ0:gmZmode = 2',
    '23:mayDecay = false']


