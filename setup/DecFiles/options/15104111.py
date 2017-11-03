# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104111.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 15104111
#
# ASCII decay Descriptor: [Lambda_b0  -> (KS0 -> pi+ pi-) p+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 15104111
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_KSppi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
