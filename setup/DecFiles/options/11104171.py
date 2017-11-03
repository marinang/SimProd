# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104171.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11104171
#
# ASCII decay Descriptor: [ B0 -> (Lambda0 -> p+ pi-) (anti-Lambda0 -> p~- pi+) ]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2LambdaX.py" )
from Configurables import Generation
Generation().EventType = 11104171
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_LambdaLambdabar=tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
