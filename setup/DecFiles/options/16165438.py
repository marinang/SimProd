# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16165438.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 16165438
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+)(a_0(980)- -> pi- eta) K-]cc
#
from Configurables import Generation
Generation().EventType = 16165438
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_LambdacKa0,pKpi,pieta=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
