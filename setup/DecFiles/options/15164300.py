# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164300.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15164300
#
# ASCII decay Descriptor: [Lambda_b0 -> ( Lambda_c+ -> ( Lambda0 -> p+ pi- ) pi+ gamma ) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164300
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacpi,Lambdapig=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
