# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26104183.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 26104183
#
# ASCII decay Descriptor: [Xi_c0 -> (Lambda0 -> p+ pi-) K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 26104183
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_LambdaKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4132,-4132 ]
