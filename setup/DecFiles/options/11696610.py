# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11696610.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11696610
#
# ASCII decay Descriptor: {[B0 -> (D*- -> pi- (anti-D0 -> K+ pi-)) (D_s+ -> pi- pi+ pi+)... ]cc}
#
from Configurables import Generation
Generation().EventType = 11696610
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstXc,Xc2hhhNneutrals=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
from Configurables import DaughtersInLHCb
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCb )
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMin = 0.
Generation().SignalRepeatedHadronization.DaughtersInLHCb.NeutralThetaMax = 10.
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
