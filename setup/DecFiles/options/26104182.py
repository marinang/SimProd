# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26104182.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 26104182
#
# ASCII decay Descriptor: [Xi_c0 -> (Lambda0 -> p+ pi-) K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 26104182
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_LambdaKK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4132,-4132 ]
