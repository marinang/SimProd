# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196121.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 11196121
#
# ASCII decay Descriptor: [B0 -> (D0 -> K- pi+) (D~0 -> K+ pi-) ( KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11196121
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0D0KS,KPi,KPi,PiPi=sqDalitz13,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
