# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11198133.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11198133
#
# ASCII decay Descriptor: [B0 -> (D*+ -> (D0 -> K- pi+) pi+) (D- -> K+ pi- pi-) (K_S0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11198133
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstDKS,D0Pi,KPiPi,PiPi=sqDalitz13,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
