# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16103330.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 16103330
#
# ASCII decay Descriptor: [Xi_b- -> (Xi- ->(Lambda0 -> p+ pi-) pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 16103330
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Xigamma=LHCbAcceptance.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
