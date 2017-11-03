# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/59990001.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 59990001
#
# ASCII decay Descriptor: rho(770)0 => (pi+ pi-)
#


from Configurables import ParticleGun, FlatNParticles, FlatPtRapidity
pgun = ParticleGun()

pgun.SignalPdgCode = 113
pgun.EventType = 59990001

pgun.SampleMass = True
pgun.MassRange_min = 300. 
pgun.MassRange_max = 4000. 

pgun.ParticleGunTool = "FlatPtRapidity"
pgun.addTool( FlatPtRapidity , name = "FlatPtRapidity" )
pgun.MassRange_min = 300. 
pgun.MassRange_max = 4000.
pgun.FlatPtRapidity.PtMin = 0.  
pgun.FlatPtRapidity.PtMax = 3500.  
pgun.FlatPtRapidity.RapidityMin = 1.8  
pgun.FlatPtRapidity.RapidityMax = 5.2  
pgun.DecayTool = "EvtGenDecay"
pgun.FlatPtRapidity.PdgCodes = [ 113 ]
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )


from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/continuum_pi+pi-.dec"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "rho(770)0 113  113  0.0 1. 0.  rho0 113  0.000000" ]
