# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11162400.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11162400
#
# ASCII decay Descriptor: [B0 -> (anti-D0 -> K+ pi-) (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11162400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pi0,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
