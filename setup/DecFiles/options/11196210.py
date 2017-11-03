# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196210.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11196210
#
# ASCII decay Descriptor: [B0 -> (D*0 -> (D0 -> K- pi+) gamma) (K*0 -> K+ pi-) (anti-D*0 -> (anti-D0 -> K+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11196210
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Dst0Kst0,D0gamma,D0gamma,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
