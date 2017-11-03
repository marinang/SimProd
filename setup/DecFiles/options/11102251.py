# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102251.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11102251
#
# ASCII decay Descriptor: {[ [B0]nos ->  (K*(1410)0 ->  K+ pi-) gamma ]cc , [[B0]os -> (K*(1410)~0 ->  K- pi+) gamma]cc}
#
from Configurables import Generation
Generation().EventType = 11102251
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst1410gamma,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
