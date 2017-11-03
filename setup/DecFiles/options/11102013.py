# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102013.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11102013
#
# ASCII decay Descriptor: [B0 -> pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11102013
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pi+pi-=CPV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
