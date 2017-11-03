# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/35103100.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 35103100
#
# ASCII decay Descriptor: [Xi- -> (Lambda0 -> p+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 35103100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xi_LambdaPi.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 3312,-3312 ]
