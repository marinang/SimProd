# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13104025.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 13104025
#
# ASCII decay Descriptor: [B_s0 -> (phi(1020) -> K+ K-) K+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 13104025
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_phiK+K-=DecProdCut,hpt400,mKKcut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

# Mass cut
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool, 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[ B_s0 => ^(phi(1020) -> ^K+ ^K-) ^K+ ^K- ]CC'
tightCut.Cuts = {
  "[K+]cc"   : "(GPT > 400 * MeV) & in_range(0.005, GTHETA, 0.400)",
  "[B_s0]cc" : "GMASS('K+' == GID, 'K-' == GID) < 2000 * MeV"
}


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 531
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 531,-531 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_531.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 13104025
