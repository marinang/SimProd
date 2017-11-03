# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16165231.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 16165231
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+)(a_1(1260)- -> pi- gamma) K- ]cc
#
from Configurables import Generation
Generation().EventType = 16165231
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_LambdacKa1,pKpi,pigamma=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
