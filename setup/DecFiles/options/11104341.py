# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104341.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11104341
#
# ASCII decay Descriptor: [B0 -> (anti-Sigma0 -> (anti-Lambda0 -> p~- pi+) gamma) p+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11104341
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Sigmappi-=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
