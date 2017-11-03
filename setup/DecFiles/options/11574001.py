# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11574001.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11574001
#
# ASCII decay Descriptor: [B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (tau+ -> mu+ nu_mu anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 11574001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstTauNu,mununu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
