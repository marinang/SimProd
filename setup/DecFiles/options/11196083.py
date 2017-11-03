# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196083.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11196083
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> pi- (D~0 -> K+ K-)) ((D+ -> pi+ pi+ K-))]cc
#
from Configurables import Generation
Generation().EventType = 11196083
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD,D0KK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
