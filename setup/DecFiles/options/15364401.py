# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15364401.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 15364401
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*(2007)0 -> {(D0 -> K- K+) (pi0 -> gamma gamma), (D0 -> K- K+) gamma} ) p+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 15364401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dst0ppi,D0,KK=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
