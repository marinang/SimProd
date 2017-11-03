# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104201.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11104201
#
# ASCII decay Descriptor: [B0 -> (phi(1020) -> K+ K-) (K*(892)0 -> K+ pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11104201
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_PhiKstgamma,KKKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
