# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16303436.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 16303436
#
# ASCII decay Descriptor: [Xi_b-  -> (N(1520)+ -> p+ pi0) K- K-]cc
#
from Configurables import Generation
Generation().EventType = 16303436
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_N+h-h-,p+pi0_PPChange=phsp,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "N(1520)+ 122 2124 1.0 1.52 5.7217391e-024 N(1520)+ 2124 0.000000e+000", "N(1520)~- 123 -2124 -1.0 1.52 5.7217391e-024 anti-N(1520)- -2124 0.000000e+000", "Xi_b- 122 5132 -1.0 6.048 1.13e-012 Xi_b- 5132 0.000000e+000", "Xi_b~+ 123 -5132 1.0 6.071 1.1e-012 anti-Xi_b+ -5132 0.000000e+000" ]
