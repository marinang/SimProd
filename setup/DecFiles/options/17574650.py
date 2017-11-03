# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17574650.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 17574650
#
# ASCII decay Descriptor: [B_s1(L)0 -> K- (B*+ ->(B+ -> D~*0 mu+ nu_mu) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 17574650
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_BstK,Dst0MuNu,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
