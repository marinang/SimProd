# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23103240.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 23103240
#
# ASCII decay Descriptor: [D_s+ -> ( eta -> pi+ pi- gamma) K+]cc
#
from Configurables import Generation
Generation().EventType = 23103240
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_etaK,pipigamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
