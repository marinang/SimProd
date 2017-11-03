# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11142401.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11142401
#
# ASCII decay Descriptor: [B0 -> (pi0 -> gamma gamma) (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) ]cc
#
from Configurables import Generation
Generation().EventType = 11142401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Jpsipi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
