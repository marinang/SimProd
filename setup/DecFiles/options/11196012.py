# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196012.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11196012
#
# ASCII decay Descriptor: [B0 -> (D+ -> K- pi+ pi+) (D~0 -> K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196012
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Dpi,KPi,KPiPi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
