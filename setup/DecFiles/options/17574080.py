# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17574080.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 17574080
#
# ASCII decay Descriptor: [B_s2*0 -> K- (B+ -> D~0 mu+ nu_mu)]cc
#
from Configurables import Generation
Generation().EventType = 17574080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs2st_BuK,D0MuNu,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 535,-535 ]
