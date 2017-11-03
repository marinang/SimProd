# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104451.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 15104451
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (phi(1020) -> pi+ pi- pi0) p+]cc
#
from Configurables import Generation
Generation().EventType = 15104451
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKphi,pipipi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
