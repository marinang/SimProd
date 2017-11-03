# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27495730.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 27495730
#
# ASCII decay Descriptor: {[ D_s2*+ -> D0 K+, D*0 K+, D+ K_S0, D*+ K_S0 ]cc}
#
from Configurables import Generation
Generation().EventType = 27495730
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2st_2710=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 435,-435 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*_s2+ 174 435 1.0 2.710 4.388079327e-24 D_s2*+ 435 0.351483","D*_s2- 178 -435 -1.0 2.710 4.388079327e-24 D_s2*- -435 0.351483" ]
