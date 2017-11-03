# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27165131.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 27165131
#
# ASCII decay Descriptor: {[ D_s2*+ -> (D*+ -> (D0 -> K- pi+) pi+) (K_S0 -> pi+ pi-) ]cc}
#
from Configurables import Generation
Generation().EventType = 27165131
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_m=3100MeV_DstKs,Dst2D0Pi,D02Kpi,Ks2PiPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 3.1 2.6328475962e-24 D_s2*+ 435 0.592116","D*_s2- 178 -435 -1.0 3.1 2.6328475962e-24 D_s2*- -435 0.592116" ]
