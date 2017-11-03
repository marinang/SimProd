# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42102200.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 42102200
#
# ASCII decay Descriptor: pp -> [Z -> (K*(892)0 -> K+ pi-) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42102200
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_Kstgamma=NoCut.dec"
Generation().Special.CutTool = ""


# Pythia8 options.
from Gaudi.Configuration import importOptions
from Configurables import Pythia8Production
importOptions('$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py')
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    'WeakSingleBoson:ffbar2gmZ = on',
    'WeakZ0:gmZmode = 2',
    '23:mayDecay = false']


