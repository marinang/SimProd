# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15436000.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 15436000
#
# ASCII decay Descriptor: {[Lambda_b0 ->  (J/psi(1S) -> K+ K- pi+ pi-) p+ K-]cc, [Lambda_b0 ->  (J/psi(1S) -> pi+ pi- pi+ pi-) p+ K-]cc, [Lambda_b0 ->  (J/psi(1S) -> K+ K- K+ K-) p+ K-]cc}
#
from Configurables import Generation
Generation().EventType = 15436000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsipK,hhhh=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
