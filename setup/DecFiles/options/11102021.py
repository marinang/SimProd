# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102021.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11102021
#
# ASCII decay Descriptor: [B0 -> K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 11102021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
