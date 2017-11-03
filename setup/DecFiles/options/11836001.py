# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11836001.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11836001
#
# ASCII decay Descriptor: {[B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (D_s+ -> nu_tau (tau+ -> pi+ pi+ pi- anti-nu_tau))]cc, [B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (D_s*+ -> gamma (D_s+ -> nu_tau (tau+ -> pi+ pi+ pi- anti-nu_tau)))]cc, [B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (D_s*+ -> pi0 (D_s+ -> nu_tau (tau+ -> pi+ pi+ pi- anti-nu_tau)))]cc}
#
from Configurables import Generation
Generation().EventType = 11836001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstDs_TauNu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
