# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27165132.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 27165132
#
# ASCII decay Descriptor: {[ D_s2*+ -> (D+ -> K- pi+ pi+) (K_S0 -> pi+ pi-) ]cc}
#
from Configurables import Generation
Generation().EventType = 27165132
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_m=2600MeV_D+Ks,D+2KPiPi,Ks2PiPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 2.6 4.388079327e-24 D_s2*+ 435 0.232766","D*_s2- 178 -435 -1.0 2.6 4.388079327e-24 D_s2*- -435 0.232766" ]
