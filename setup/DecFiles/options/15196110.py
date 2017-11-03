# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15196110.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15196110
#
# ASCII decay Descriptor: [Lambda_b0 -> (psi(3770) ->  (D0 -> K- pi+) (D0bar -> K+ pi-) ) (Lambda0 -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15196110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_psi3770Lambda,D0D0bar,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
