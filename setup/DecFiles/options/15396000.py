# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15396000.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15396000
#
# ASCII decay Descriptor: [Lambda_b0 -> K- (Lambda_c+ -> p+ K- pi+) (anti-D0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15396000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcD0K,Lc_pKpi,D0_Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
