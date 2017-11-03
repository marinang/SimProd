# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104451.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11104451
#
# ASCII decay Descriptor: [B0 -> (a_10 -> pi+ pi- pi0) (phi -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 11104451
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_a10phi,pipip0KK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
