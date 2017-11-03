# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11398001.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11398001
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (anti-D0 -> K+ pi+ pi- pi-) pi-) ( (D+ -> pi+ K+ K-) || (D+ -> K- pi+ pi+ ) ) ]cc
#
from Configurables import Generation
Generation().EventType = 11398001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD,D0K3pi,Dkhh=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
