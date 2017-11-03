# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196010.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11196010
#
# ASCII decay Descriptor: [B0 -> (D- -> K+ pi- pi-) (D0 -> K- pi+) K+]cc
#
from Configurables import Generation
Generation().EventType = 11196010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DD0K,Kpipi,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
