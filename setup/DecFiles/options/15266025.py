# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15266025.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 15266025
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c*0 -> (Lambda_c+ -> p+ K- pi+) pi-) K- K+]cc
#
from Configurables import Generation
Generation().EventType = 15266025
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ScstKK,Lcpi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
