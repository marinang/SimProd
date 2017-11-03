# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15396200.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 15396200
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (Lambda_c+ -> p+ K- pi+) (anti-D*0 -> (anti-D0 ->  K+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15396200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDstK,Lc_pKpi,Dst_D0gamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
