# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15364420.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 15364420
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*(2007)0 -> {(D0 -> K- K+) (pi0 -> gamma gamma), (D0 -> K- K+) gamma} ) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15364420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dst0pK,D0,KK=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
