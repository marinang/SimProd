# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16146111.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 16146111
#
# ASCII decay Descriptor: [Sigma_b0 -> (Xi_b- -> (Xi- -> Lambda0 pi-) (J/psi(1S) -> mu+ mu-) )pi+]cc
#
from Configurables import Generation
Generation().EventType = 16146111
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibstar0_Xibpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5212,-5212 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b0   112   5212  0.0  6.00000  6.000000e-020       Sigma_b0   5212  1.000000e-004", " Sigma_b~0  113  -5212  0.0  6.00000  6.000000e-020  anti-Sigma_b0  -5212  1.000000e-004" ]
