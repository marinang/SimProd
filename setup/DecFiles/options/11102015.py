# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102015.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11102015
#
# ASCII decay Descriptor: [B0 -> pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11102015
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pi+pi-=CPV2017,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
