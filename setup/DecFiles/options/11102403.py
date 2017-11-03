# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102403.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11102403
#
# ASCII decay Descriptor: {[[B0]nos -> pi+ pi- (pi0 -> gamma gamma)]cc, [[B0]os -> pi- pi+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11102403
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pi+pi-pi0=sqDalitz.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
