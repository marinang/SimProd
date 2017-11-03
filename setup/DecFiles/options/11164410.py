# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164410.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11164410
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) (K*(892)+ -> K+ (pi0 -> gamma gamma))]cc, [[B0]os -> (D+ => K- pi+ pi+) (K*(892)+ -> K- (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11164410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-Kst+,Kpipi,Kpi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
