# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16265026.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 16265026
#
# ASCII decay Descriptor: [Sigma_b+ -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+ ) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 16265026
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sb+_Lbpi,Lcpi_3=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5222,-5222 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_b+    110   5222   1.0      6.095      2.1940397e-23                  Sigma_b+        5222      0.25000000","Sigma_b~-   111  -5222  -1.0      6.095  2.1940397e-23             anti-Sigma_b-       -5222      0.25000000" ]
