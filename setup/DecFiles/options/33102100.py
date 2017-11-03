# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/33102100.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 33102100
#
# ASCII decay Descriptor: [Lambda0 -> pi- p+]cc
#
from Configurables import Generation
Generation().EventType = 33102100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Lambda,ppi.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 3122,-3122 ]
