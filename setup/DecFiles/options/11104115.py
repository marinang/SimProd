# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104115.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11104115
#
# ASCII decay Descriptor: [B0 -> (eta_prime -> rho0 gamma) (Kst -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104115
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapKst,rhogamma=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
