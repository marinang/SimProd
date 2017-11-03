# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23123011.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 23123011
#
# ASCII decay Descriptor: [D_s+ -> pi- e+ e+]cc
#
from Configurables import Generation
Generation().EventType = 23123011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_pi-ee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
