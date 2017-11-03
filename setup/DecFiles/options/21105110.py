# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21105110.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 21105110
#
# ASCII decay Descriptor: [D+ -> (KS0 -> pi+ pi-) K+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 21105110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_KsK+pi-pi+=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
