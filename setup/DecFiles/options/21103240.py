# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21103240.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 21103240
#
# ASCII decay Descriptor: [D+ -> ( eta -> pi+ pi- gamma) pi+]cc
#
from Configurables import Generation
Generation().EventType = 21103240
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_etapi,pipigamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
