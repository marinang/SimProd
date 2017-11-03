# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144071.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11144071
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 11144071
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
