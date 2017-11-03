# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166162.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11166162
#
# ASCII decay Descriptor: {[[B0]nos => (K_S0 -> pi+ pi-) (D- => K+ pi- pi-) K+]cc, [[B0]os => (K_S0 -> pi+ pi-) (D+ => K- pi+ pi+) K-]cc}
#
from Configurables import Generation
Generation().EventType = 11166162
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-KSK,Kpipi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
