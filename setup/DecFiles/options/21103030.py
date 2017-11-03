# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21103030.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 21103030
#
# ASCII decay Descriptor: [D+ -> K- pi+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 21103030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K-pi+pi+=phsp.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
