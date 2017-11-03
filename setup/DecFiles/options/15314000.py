# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15314000.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15314000
#
# ASCII decay Descriptor: {[Lambda_b0 ->  e- mu+  (Lambda(1520)0 -> p+ K-)]cc,[Lambda_b0 ->  e+ mu- (Lambda(1520)0 -> p+ K-)]cc}
#
from Configurables import Generation
Generation().EventType = 15314000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambda1520emu,pK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
