# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15574080.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15574080
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (D0 -> K- pi+) p+) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15574080
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0pmunu,D0_Kpi=LHCbAcceptance.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+   62   4122   1.0   2.840   2.0e-24  Lambda_c+   4122   0.0", "Lambda_c~-   63   -4122  -1.0   2.840   2.0e-24   anti-Lambda_c-   -4122   0.0" ]
