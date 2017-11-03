# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26104180.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 26104180
#
# ASCII decay Descriptor: [Xi_c0 -> (Xi- ->(Lambda0 -> p+ pi-) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 26104180
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_Xipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 4132,-4132 ]
