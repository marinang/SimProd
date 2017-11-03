# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25105100.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 25105100
#
# ASCII decay Descriptor: [Lambda_c+ -> (Lambda0 -> p+ pi-) pi+ pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 25105100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_Lambdapipipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
