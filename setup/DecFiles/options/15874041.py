# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15874041.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 15874041
#
# ASCII decay Descriptor: [[Lambda_b0] -> (Lambda_c+ -> p+  K- pi+)  anti-nu_mu mu-]cc
#
from Configurables import Generation
Generation().EventType = 15874041
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lcmunu,pKpi=cocktail,Baryonlnu.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
