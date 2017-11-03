# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16166043.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 16166043
#
# ASCII decay Descriptor: [Xi_b0 -> (D+ --> K- pi+ pi+) p+ K- pi-]CC
#
from Configurables import Generation
Generation().EventType = 16166043
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_D+pK-pi-=phsp.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
