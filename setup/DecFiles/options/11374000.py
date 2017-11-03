# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11374000.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11374000
#
# ASCII decay Descriptor: {[B0 -> (D~0 -> K+ pi-) e+ mu-]cc,[B0 -> (D~0 -> K+ pi-) e- mu+]cc}
#
from Configurables import Generation
Generation().EventType = 11374000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0emu,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
