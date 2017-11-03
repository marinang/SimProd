# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15296000.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 15296000
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s- => K+ K- pi-) (Lambda_c+ -> p K- pi+)]cc
#
from Configurables import Generation
Generation().EventType = 15296000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_DsLambdac.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
