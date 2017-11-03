# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11198135.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11198135
#
# ASCII decay Descriptor: [B0 -> (D_s+ -> K+ K- pi+) (D_s- -> K+ K- pi-)  ( KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11198135
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsDsKS,KKPi,KKPi,PiPi=sqDalitz13,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
