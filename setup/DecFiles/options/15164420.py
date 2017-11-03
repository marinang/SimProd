# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164420.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 15164420
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ pi- (D0 -> K- pi+ pi0)]cc
#
from Configurables import Generation
Generation().EventType = 15164420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0ppi,Kpipi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
