# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166761.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11166761
#
# ASCII decay Descriptor: {[[B0]nos => (K_S0 -> pi+ pi-) (D*(2010)- -> {(D- => K+ pi- pi-)pi0, (D- => K+ pi- pi-)gamma}) pi+]cc, [[B0]os => (K_S0 -> pi+ pi-) (D*(2010)+ -> {(D+ => K- pi+ pi+)pi0, (D+ => K+ pi- pi-)gamma}) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11166761
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-KSpi,Kpipi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
