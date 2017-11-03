# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102421.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11102421
#
# ASCII decay Descriptor: {[[B0]nos -> K+ K- (pi0 -> gamma gamma)]cc, [[B0]os -> K- K+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102421
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+K-pi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
