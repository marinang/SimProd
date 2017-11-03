# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22214000.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 22214000
#
# ASCII decay Descriptor: [D0 => K- pi+ mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22214000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_Kpimumu=res,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "rho(770)0_nocut 1033 200113 0.0 0.771100 4.411610e-024 rho0_nocut 200113 0.0e+00","omega(782)_nocut 1036 200223  0.0 0.782570 7.798723e-023 omega_nocut 200223 0.0" ]
