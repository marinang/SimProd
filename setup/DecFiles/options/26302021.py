# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26302021.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 26302021
#
# ASCII decay Descriptor: {[Sigma_c++ -> p+ p+]cc, [Sigma_c++ -> p+ p+ K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 26302021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Hc++_pp=DecProdCut,m=3220MeV,t=0.2ps,PPChange.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 4222,-4222 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c++ 85 4222 2.0 3.220 2.e-13 Sigma_c++ 4222 0." , "Sigma_c~-- 86 -4222 -2.0 3.220 2.e-13 anti-Sigma_c-- -4222 0." ]
