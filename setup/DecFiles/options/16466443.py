# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16466443.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 16466443
#
# ASCII decay Descriptor: [Xi_b0 -> ( D*+ -> (D+ --> K- pi+ pi+) pi0, gamma )  p+ K- pi-]CC
#
from Configurables import Generation
Generation().EventType = 16466443
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_Dst+pK-pi-=phsp.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
