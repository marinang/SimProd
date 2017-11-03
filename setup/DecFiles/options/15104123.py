# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104123.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15104123
#
# ASCII decay Descriptor: [Lambda_b0  -> (Lambda0 -> p+ pi-) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2KShh.py" )
from Configurables import Generation
Generation().EventType = 15104123
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdapipi=sqDalitz,tightCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
