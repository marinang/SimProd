# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104170.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11104170
#
# ASCII decay Descriptor: [ B0 -> (Lambda0 -> p+ pi-) (anti-Lambda0 -> p~- pi+) ]cc
#
from Configurables import Generation
Generation().EventType = 11104170
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_LambdaLambda.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
