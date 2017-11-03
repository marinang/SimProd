# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15396400.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 15396400
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (Lambda_c+ -> p+ K- pi+) (anti-D*0 -> (anti-D0 ->  K+ pi-) pi0)]cc
#
from Configurables import Generation
Generation().EventType = 15396400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDstK,Lc_pKpi,Dst_D0pi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
