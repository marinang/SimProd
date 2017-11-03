# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/32103002.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 32103002
#
# ASCII decay Descriptor: [Sigma+ -> p+ p+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 32103002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Hs+_pppi=DecProdCut,m=2030MeV,t=100ps,PPChange.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3222,-3222 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma+ 19 3222 1.0 2.030 100.e-12 Sigma+ 3222 0." , "Sigma~- 27 -3222 -1.0 2.030 100.e-12 anti-Sigma-  -3222 0." ]
