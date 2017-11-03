# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164130.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15164130
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) pi+) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164130
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacpi,Lambdapi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
