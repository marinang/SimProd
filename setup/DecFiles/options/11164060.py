# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164060.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11164060
#
# ASCII decay Descriptor: {[[B0]nos => pi+ pi- (D~0 -> K+ pi-)]cc, [[B0]os => pi- pi+ (D0 -> K- pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11164060
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0pipi,Kpi=PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
