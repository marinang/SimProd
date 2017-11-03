# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21263002.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 21263002
#
# ASCII decay Descriptor: [D+ -> K- K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 21263002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_K-K+pi+=res,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
