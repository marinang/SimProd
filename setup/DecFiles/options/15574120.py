# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574120.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 15574120
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) mu+ nu_mu)  anti-nu_e e-]cc
#
from Configurables import Generation
Generation().EventType = 15574120
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcenu,L0munu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
