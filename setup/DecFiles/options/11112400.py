# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11112400.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11112400
#
# ASCII decay Descriptor: [B0 -> mu+ mu- (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11112400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pimumu=MS,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
