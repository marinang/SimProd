# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104503.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11104503
#
# ASCII decay Descriptor: [B0 -> K+ K- (K*0 -> (K_S0 -> pi+ pi-) (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 11104503
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst0KK,KSpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
