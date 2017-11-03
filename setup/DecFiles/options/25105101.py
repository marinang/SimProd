# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25105101.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 25105101
#
# ASCII decay Descriptor: [Lambda_c+ -> (Xi- -> (Lambda0 -> p+ pi-) pi-) K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 25105101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_XiKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
