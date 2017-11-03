# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16104146.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 16104146
#
# ASCII decay Descriptor: [Xi_b0  -> K+ pi- ( Lambda0 -> p+ pi- )]cc
#
from Configurables import Generation
Generation().EventType = 16104146
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_LambdaKpi,ppi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
