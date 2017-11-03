# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16103034.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 16103034
#
# ASCII decay Descriptor: [Xi_b-  -> K- K- p+]cc
#
from Configurables import Generation
Generation().EventType = 16103034
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_KKp=sqDalitz,OmegabIsXib,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b- 122 5132 -1.0 6.046 1.66e-012 Xi_b- 5132 0.000000e+000", "Xi_b~+ 123 -5132 1.0 6.046 1.66e-012 anti-Xi_b+ -5132 0.000000e+000" ]
