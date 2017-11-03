# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164121.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 15164121
#
# ASCII decay Descriptor: [Lambda_b0 -> (anti-D0 -> K+ pi-) (Lambda -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15164121
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_antiD0Lambda,Kpippi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
