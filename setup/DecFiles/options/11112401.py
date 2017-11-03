# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11112401.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11112401
#
# ASCII decay Descriptor: [B0 -> mu+ mu- (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11112401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pimumu=btosllball05,DiLeptonInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
