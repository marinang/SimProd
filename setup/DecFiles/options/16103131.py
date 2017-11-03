# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16103131.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 16103131
#
# ASCII decay Descriptor: [Xi_b- -> pi- (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 16103131
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Lambdapi,ppi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
