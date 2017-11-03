# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16264042.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 16264042
#
# ASCII decay Descriptor: [Xi_b0 -> (Xi_c+ -> p K+ pi-) K-]cc
#
from Configurables import Generation
Generation().EventType = 16264042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_XicK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
