# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104131.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11104131
#
# ASCII decay Descriptor: {[B0 -> K+ pi- (KS0 -> pi+ pi-)]cc, [B0 -> K- pi+ (KS0 -> pi+ pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 11104131
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KpiKS=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
