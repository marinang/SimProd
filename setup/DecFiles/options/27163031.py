# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163031.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 27163031
#
# ASCII decay Descriptor: {[ D_s2*+ -> (D0 -> K- pi+) K+ ]cc}
#
from Configurables import Generation
Generation().EventType = 27163031
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_m=3000MeV_D0K,D02KPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 3.0 2.6328475962e-24 D_s2*+ 435 0.641483","D*_s2- 178 -435 -1.0 3.0 2.6328475962e-24 D_s2*- -435 0.641483" ]
