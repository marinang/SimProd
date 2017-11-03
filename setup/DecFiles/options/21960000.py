# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21960000.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 21960000
#
# ASCII decay Descriptor: [D+ -> ...]cc
#
from Configurables import Generation
Generation().EventType = 21960000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+,incl.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
