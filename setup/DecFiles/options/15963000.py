# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15963000.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 15963000
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c(2593)+ -> (Sigma_c0 -> MyLambda_c+ pi-) pi+) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15963000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593munu,Sigmacpi,Lcpi=NoCut.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
