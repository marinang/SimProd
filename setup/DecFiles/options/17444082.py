# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17444082.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 17444082
#
# ASCII decay Descriptor: [B*_s20 ->  (B+ -> K+ (J/psi(1S) -> mu+ mu-)) K-]cc, [B*_s20 ->  (B+ -> pi+ (anti-D0 -> K+ pi-)) K-]cc, [B*_s20 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) K-]cc, [B_s2*0 -> K- (B*+ -> (B+ -> (anti-D0 -> K+ pi-) pi+) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 17444082
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bsstst_BuK,JpsiK,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 535,-535 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B*_s20 212 535 0.0 6.0729600 4.113825e-22 B_s2*0 535 0.000000", "B*_s2~0 216 -535 0.0 6.0729600 4.113825e-22 anti-B_s2*0 -535 0.000000" ]
