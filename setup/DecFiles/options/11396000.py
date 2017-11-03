# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11396000.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11396000
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> pi- (D~0 -> K+ pi-)) ((D+ -> pi+ pi+ K-) || (D+ -> K+ pi+ K-) || (D+ -> pi+ K+ K-) || (D+ -> pi+ pi+ pi-))]cc
#
from Configurables import Generation
Generation().EventType = 11396000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstD=DDALITZ,DecProdCut,CPV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
