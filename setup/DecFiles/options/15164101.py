# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164101.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 15164101
#
# ASCII decay Descriptor: [Lambda_b0 -> ( Xi_c+ -> ( Lambda0 -> p+ pi- ) pi+ ) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Xicpi,Lambdapi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
