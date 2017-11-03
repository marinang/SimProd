# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196101.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11196101
#
# ASCII decay Descriptor: [B0 -> (D0 -> K- pi+) (D~0 -> K+ pi-) ( KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11196101
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0D0KS,KPi,KPi,PiPi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
