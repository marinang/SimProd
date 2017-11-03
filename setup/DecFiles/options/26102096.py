# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26102096.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 26102096
#
# ASCII decay Descriptor: [Xi_c+ -> Sigma+ K+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 26102096
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_SigmaKK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4232,-4232 ]
