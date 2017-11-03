# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166061.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11166061
#
# ASCII decay Descriptor: {[[B0]nos => pi+ pi- (D~0 -> K+ pi- pi+ pi-)]cc, [[B0]os => pi- pi+ (D0 -> K- pi+ pi- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11166061
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pipi,K3pi=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
