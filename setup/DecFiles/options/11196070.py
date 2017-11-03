# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196070.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11196070
#
# ASCII decay Descriptor: [B0 -> (psi(3770) ->  (D0 -> K- pi+) (D0bar -> K+ pi-) ) K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196070
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi3770Kpi,D0D0bar,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
