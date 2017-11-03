# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11266412.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11266412
#
# ASCII decay Descriptor: [B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) pi+ pi+ pi- pi0]cc
#
from Configurables import Generation
Generation().EventType = 11266412
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstpipipipi0withRho2S=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
