# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11714000.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11714000
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ (tau- -> mu- anti-nu_mu nu_tau) (K*(892)0 -> K+ pi-)]cc, [[B0]nos -> (tau+ -> mu+ nu_mu anti-nu_tau) mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- (tau+ -> mu+ nu_mu anti-nu_tau) (K*(892)~0 -> K- pi+)]cc, [[B0]os -> (tau- -> mu- anti-nu_mu nu_tau) mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11714000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksttaumu,mu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
