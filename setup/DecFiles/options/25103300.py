# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103300.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 25103300
#
# ASCII decay Descriptor: [Lambda_c+ -> (Sigma0 ->(Lambda0 -> p+ pi-) gamma) pi+]cc
#
from Configurables import Generation
Generation().EventType = 25103300
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_Sigmapi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
