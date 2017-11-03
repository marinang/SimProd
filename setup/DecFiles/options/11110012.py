# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11110012.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11110012
#
# ASCII decay Descriptor: {[[B0]nos -> mu+ (tau- -> pi+ pi- pi- nu_tau) (K*(892)0 -> K+ pi-)]cc, [[B0]nos -> (tau+ -> pi+ pi- pi+ anti-nu_tau) mu- (K*(892)0 -> K+ pi-)]cc, [[B0]os -> mu- (tau+ -> pi+ pi- pi+ anti-nu_tau) (K*(892)~0 -> K- pi+)]cc, [[B0]os -> (tau- -> pi+ pi- pi- nu_tau) mu+ (K*(892)~0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11110012
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Ksttaumu,3pi=DecProdCut,tauolacleo.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
