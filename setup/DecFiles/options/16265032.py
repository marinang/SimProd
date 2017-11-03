# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16265032.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 16265032
#
# ASCII decay Descriptor: [Xi_b- -> (Xi_c0 -> p K- K- pi+) K-]cc
#
from Configurables import Generation
Generation().EventType = 16265032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Xic0K=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
