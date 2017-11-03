# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16145134.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 16145134
#
# ASCII decay Descriptor: [Xi_b- -> (Omega- -> (Lambda0 -> p+ pi-) K-) (J/psi(1S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 16145134
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_JpsiOmega,mm,LambdaK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b-  122   5132 -1.0  6.050000   1.390000e-012  Xi_b- 5132  0.000000e+000",  "Xi_b~+ 123 -5132  1.0  6.050000   1.390000e-012 anti-Xi_b+    -5132   0.000000e+000", "Omega-                 24        3334  -1.0      1.67245000      8.210e-11  Omega-        3334      0.00000000", "Omega~+                32       -3334   1.0      1.67245000      8.210e-11               anti-Omega+       -3334      0.00000000", "Xi'_b-                116        5312  -1.0      6.25000000      1.000000e-19                    Xi'_b-        5312      0.00010000", "Xi'_b~+               117       -5312   1.0      6.25000000      1.000000e-19               anti-Xi'_b+       -5312      0.00010000", "Xi_b*-                538        5314  -1.0      6.26000000      0.000000e+00                    Xi_b*-        5314      0.00000000", "Xi_b*~+               539       -5314   1.0      6.26000000      0.000000e+00               anti-Xi_b*+       -5314      0.00000000" ]
