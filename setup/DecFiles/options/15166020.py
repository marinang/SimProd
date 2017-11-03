# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15166020.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 15166020
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> K- pi+ pi- pi+) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15166020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0pK,K3pi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
