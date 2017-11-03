# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/59984000.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 59984000
#
# ASCII decay Descriptor: [continuum] => ( D0 -> K- pi+ ) ( D~0 -> K+ pi- )
#


from Configurables import ParticleGun, FlatNParticles, FlatPtRapidity
# Prepare particle gun
pgun = ParticleGun()

pgun.SignalPdgCode = 12345

pgun.SampleMass = True
pgun.MassRange_min = 4000. 
pgun.MassRange_max = 8000. 

pgun.ParticleGunTool = "FlatPtRapidity"
pgun.addTool( FlatPtRapidity , name = "FlatPtRapidity" )
pgun.FlatPtRapidity.OutputLevel = 0 # Make debug
pgun.MassRange_min = 3730 
pgun.MassRange_max = 5500
pgun.FlatPtRapidity.PtMin = 0  
pgun.FlatPtRapidity.PtMax = 4000  
pgun.FlatPtRapidity.RapidityMin = 1.8  
pgun.FlatPtRapidity.RapidityMax = 4.7  
pgun.DecayTool = "EvtGenDecay"
pgun.FlatPtRapidity.PdgCodes = [ 12345 ]
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )


from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ContinuumDD,KPi,KPi=NoCut.dec"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "  M 1234  12345  0.0 1.0 0.000000e+00  M 12345  0.000000" ]
