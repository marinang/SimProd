# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11134080.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11134080
#
# ASCII decay Descriptor: {[ B0 -> (eta_c(1S) -> p+ p~-) K+ K-]cc}
#
from Configurables import Generation
Generation().EventType = 11134080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etacKK,pp=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
