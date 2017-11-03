# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103005.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 25103005
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 25103005
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_pphi,KK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+  62  4122  1.0  2.468 4.400000e-013 Lambda_c+  4122  0", "Lambda_c~-  63 -4122 -1.0  2.468 4.400000e-013  anti-Lambda_c-  -4122   0." ]
