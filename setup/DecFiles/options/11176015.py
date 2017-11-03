# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11176015.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11176015
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> pi- (D~0 -> K+ pi-)) mu+ (N-> mu+ pi-) {,gamma}{,gamma}]cc
#
from Configurables import Generation
Generation().EventType = 11176015
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dstmumupi,mN=3100MeV=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "N 1235 19 0.0 3.1 0 N 19 0.0","anti-N 1236 -19 0.0 3.1 0 anti-N -19 0.0" ]
