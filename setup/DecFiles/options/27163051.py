# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163051.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 27163051
#
# ASCII decay Descriptor: {[ D*_2(2460)+ -> (D0 -> K- pi+) pi+ ]cc}
#
from Configurables import Generation
Generation().EventType = 27163051
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D2st_m=2700MeV_D0Pi,D02KPi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 415,-415 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_2(2460)+ 162 415 1.0 2.7 2.6328475962e-24 D_2*+ 415 0.69558982","D*_2(2460)- 158 -415 -1.0 2.7 2.6328475962e-24 D_2*- -415 0.69558982" ]
