# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104212.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 15104212
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (eta' -> (rho0 -> pi+ pi-) gamma) p+]cc
#
from Configurables import Generation
Generation().EventType = 15104212
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKetap,rhogamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
