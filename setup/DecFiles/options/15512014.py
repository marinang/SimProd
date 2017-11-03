# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15512014.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 15512014
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15512014
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pmunu=DecProdCut,LQCD.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
