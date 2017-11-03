# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16103032.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 16103032
#
# ASCII decay Descriptor: [Xi_b-  -> pi- pi- p+]cc
#
from Configurables import Generation
Generation().EventType = 16103032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_pipip=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
