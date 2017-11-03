# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164601.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15164601
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*(2007)0 -> {(D0 -> K- pi+) (pi0 -> gamma gamma), (D0 -> K- pi+) gamma} ) p+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 15164601
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dst0ppi,D0=sqDalitz,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
