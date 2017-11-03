# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163231.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 27163231
#
# ASCII decay Descriptor: [D*+ -> ( D0 -> (rho0 -> pi+ pi-) gamma ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27163231
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,rhogamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
