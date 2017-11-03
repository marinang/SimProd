# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16165034.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 16165034
#
# ASCII decay Descriptor: [Xi_b- -> (Lambda_c+ -> p K- pi+) pi- pi-]cc
#
from Configurables import Generation
Generation().EventType = 16165034
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_Lambdacpipi,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b- 122 5132 -1.0 6.071 1.1e-012 Xi_b- 5132 0.000000e+000", "Xi_b~+ 123 -5132 1.0 6.071 1.1e-012 anti-Xi_b+ -5132 0.000000e+000" ]
