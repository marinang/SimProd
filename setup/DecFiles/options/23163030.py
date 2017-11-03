# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23163030.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 23163030
#
# ASCII decay Descriptor: [D_s+ -> K+ K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 23163030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_KKpi.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
