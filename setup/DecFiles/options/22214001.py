# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22214001.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 22214001
#
# ASCII decay Descriptor: [D0 => K+ K- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22214001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_KKmumu=res,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "rho(770)0_nocut 1033 200113 0.0 0.771100 4.411610e-024 rho0_nocut 200113 0.0e+00", "phi(1020)_nocut 1037 200333 0.0 1.019456 1.545099e-022 phi_nocut 200333 0.0" ]
