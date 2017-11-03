# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16145032.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 16145032
#
# ASCII decay Descriptor: [anti-Xi_b+ -> (J/psi(1S) -> mu+ mu-) (phi -> K+ K-) p+]cc
#
from Configurables import Generation
Generation().EventType = 16145032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/X5835+_Jpsiphip,mumu=phsp,DecProdCut,PPChange.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b-  122  5132  -1.0  5.835 1.5e-012      Xi_b-   5132  0.00000000", "Xi_b~+  123  -5132  1.0  5.835  1.5e-012 anti-Xi_b+  -5132  0.00000000" ]
