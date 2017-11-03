# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11198134.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11198134
#
# ASCII decay Descriptor: [B0 -> ( D*+ -> (D0 -> K- pi+) pi+) (D*- -> (D~0 -> K+ pi-) pi-)  ( KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11198134
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstDstKS,D0Pi,D0Pi,PiPi=sqDalitz13,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
