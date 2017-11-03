# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/33512001.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 33512001
#
# ASCII decay Descriptor: [Lambda0 -> p+ mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 33512001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lambda_pmunu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3122,-3122 ]
