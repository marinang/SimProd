# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11184000.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11184000
#
# ASCII decay Descriptor: [B0 -> (D~0 -> K+ pi-) e- e+]cc
#
from Configurables import Generation
Generation().EventType = 11184000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0ee,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
