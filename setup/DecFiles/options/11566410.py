# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11566410.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11566410
#
# ASCII decay Descriptor: [B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (tau+ -> pi+ pi+ pi- pi0 anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 11566410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstTauNu,Tau2PiPiPiPi0Nu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
