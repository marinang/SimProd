# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15114113.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15114113
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) e+ mu-]
#
from Configurables import Generation
Generation().EventType = 15114113
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdaemu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
