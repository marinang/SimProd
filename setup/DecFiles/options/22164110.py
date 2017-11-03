# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22164110.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 22164110
#
# ASCII decay Descriptor: [D0 -> (KS0 -> pi+ pi-) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 22164110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_KSKS=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
