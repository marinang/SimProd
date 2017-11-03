# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16102041.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 16102041
#
# ASCII decay Descriptor: [Xi_b0 -> p+ K-]cc
#
from Configurables import Generation
Generation().EventType = 16102041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_pK=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
