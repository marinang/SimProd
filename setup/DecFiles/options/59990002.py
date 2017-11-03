# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/59990002.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 59990002
#
# ASCII decay Descriptor: M => (mu+ mu-)
#


from Configurables import ParticleGun, FlatNParticles, FlatPtRapidity
pgun = ParticleGun()
pgun.OutputLevel = 1

pgun.SignalPdgCode = 12345
pgun.EventType = 59990002

pgun.SampleMass = True
pgun.MassRange_min = 1500. 
pgun.MassRange_max = 20000. 

pgun.ParticleGunTool = "FlatPtRapidity"
pgun.addTool( FlatPtRapidity , name = "FlatPtRapidity" )
pgun.FlatPtRapidity.OutputLevel = 0
pgun.FlatPtRapidity.PtMin = 0.  
pgun.FlatPtRapidity.PtMax = 2000.  
pgun.FlatPtRapidity.RapidityMin = 1.8  
pgun.FlatPtRapidity.RapidityMax = 5.2 
pgun.DecayTool = "EvtGenDecay"
pgun.FlatPtRapidity.PdgCodes = [ 12345 ]
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )


from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/continuum_mu+mu-.dec"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "  M 1234  12345  0.0 1.0 0.000000e+00  M 12345  0.000000" ]
