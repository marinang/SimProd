# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103100.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 25103100
#
# ASCII decay Descriptor: [Lambda_c+ -> (KS0 -> pi+ pi-) p+]cc
#
from Configurables import Generation
Generation().EventType = 25103100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_KSp=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
