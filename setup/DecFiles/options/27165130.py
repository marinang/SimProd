# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27165130.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 27165130
#
# ASCII decay Descriptor: {[ D_s2*+ -> (D*+ -> (D0 -> K- pi+) pi+) (K_S0 -> pi+ pi-) ]cc}
#
from Configurables import Generation
Generation().EventType = 27165130
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_m=2700MeV_DstKs,Dst2D0Pi,D02Kpi,Ks2PiPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 2.7 4.388079327e-24 D_s2*+ 435 0.192116","D*_s2- 178 -435 -1.0 2.7 4.388079327e-24 D_s2*- -435 0.192116" ]
