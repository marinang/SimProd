# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16875001.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 16875001
#
# ASCII decay Descriptor: [Sigma_b- -> K- (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+) mu- anti-nu_mu)]cc
#
from Configurables import Generation
Generation().EventType = 16875001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/XibStar2_LbK,Lcmunu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5112,-5112 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b-   114   5112 -1.0  6.228  6.000000e-020       Sigma_b-   5112  1.000000e-004", " Sigma_b~+  115  -5112  1.0  6.228  6.000000e-020  anti-Sigma_b+  -5112  1.000000e-004", " Xi_b0   124   5232  0.0  5.7918  1.480000e-012       Xi_b0   5232  0.000000e+000", " Xi_b~0  125  -5232  0.0  5.7918  1.480000e-012  anti-Xi_b0  -5232  0.000000e+000" ]
