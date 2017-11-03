# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11162410.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11162410
#
# ASCII decay Descriptor: [B0 -> (anti-D0 -> K+ K-) (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11162410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pi0,KK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
