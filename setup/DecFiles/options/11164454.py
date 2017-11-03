# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164454.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11164454
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => (phi -> K+ K-) (rho- -> pi- pi0)) pi+]cc, [[B0]os -> (D+ => (phi -> K+ K-) (rho+ -> pi+ pi0)) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11164454
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dpi,phirho=SVV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
