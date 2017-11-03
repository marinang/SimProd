# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15366013.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 15366013
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s+ => K+ K- pi+)  p K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 15366013
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_DspKpi,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
