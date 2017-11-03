# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23113015.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 23113015
#
# ASCII decay Descriptor: [D_s+ -> K+ mu+ e-]cc
#
from Configurables import Generation
Generation().EventType = 23113015
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_K+mue=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
