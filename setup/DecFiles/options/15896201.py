# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15896201.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15896201
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s*- -> (D_s- -> (tau- -> mu- anti-nu_mu nu_tau) anti-nu_tau) gamma) (Lambda_c(2625)+ -> (Lambda_c+ -> p+ K- pi+) pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15896201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2625Dsst,Lcpipi,ppiK,semileptonic=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
