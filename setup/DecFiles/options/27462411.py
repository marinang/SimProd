# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27462411.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 27462411
#
# ASCII decay Descriptor: [D*(2007)0 -> (D0 -> {K- pi+}) (pi0,gamma)]cc
#
from Configurables import Generation
Generation().EventType = 27462411
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst0_D0pi0_D0gamma,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]
