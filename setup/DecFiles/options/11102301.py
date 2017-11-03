# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102301.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11102301
#
# ASCII decay Descriptor: [B0 -> (eta_prime -> rho0 gamma) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11102301
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapKS,rhogamma=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
