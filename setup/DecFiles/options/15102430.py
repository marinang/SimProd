# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15102430.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 15102430
#
# ASCII decay Descriptor: [ Lambda_b0 -> p+ K- pi0 ]cc
#
from Configurables import Generation
Generation().EventType = 15102430
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKpi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
