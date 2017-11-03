# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104130.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 15104130
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p+ KS0) K-]cc
#
from Configurables import Generation
Generation().EventType = 15104130
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LambdacK,pKS=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
