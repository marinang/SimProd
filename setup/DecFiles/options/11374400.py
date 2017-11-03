# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11374400.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11374400
#
# ASCII decay Descriptor: {[B0 -> (D*(2007)~0 -> (D~0 -> K+ pi-) pi0) e+ mu-]cc,[B0 -> (D*(2007)~0 -> (D~0 -> K+ pi-) pi0) e- mu+]cc}
#
from Configurables import Generation
Generation().EventType = 11374400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0emu,D0pi,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
