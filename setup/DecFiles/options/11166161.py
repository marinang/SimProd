# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166161.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11166161
#
# ASCII decay Descriptor: {[[B0]nos => (K_S0 -> pi+ pi-) (D- => K+ pi- pi-) pi+]cc, [[B0]os => (K_S0 -> pi+ pi-) (D+ => K- pi+ pi+) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11166161
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-KSpi,Kpipi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
