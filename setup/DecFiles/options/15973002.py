# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15973002.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 15973002
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c(2593)+ -> (Sigma_c0 -> MyLambda_c+ pi-) pi+) tau- anti-nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 15973002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593taunu,Sigmacpi,Lcpi=NoCut.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
