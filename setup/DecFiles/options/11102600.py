# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102600.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11102600
#
# ASCII decay Descriptor: [B0 -> (omega(782) -> pi+ pi- (pi0 -> gamma gamma) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11102600
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_omegagamma.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
