# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196211.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11196211
#
# ASCII decay Descriptor: [B0 -> K+ (D*0 -> (D0 -> K- pi+) gamma) (anti-D*0 -> (anti-D0 -> K+ pi-) gamma) pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196211
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Dst0Kpi,D0gamma,D0gamma,Kpi=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
