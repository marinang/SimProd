# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164452.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11164452
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => (phi -> K+ K-) (rho- -> pi- pi0)) pi+]cc, [[B0]os -> (D_s+ => (phi -> K+ K-) (rho+ -> pi+ pi0)) pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11164452
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dspi,phirho=SVV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
