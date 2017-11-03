# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13574086.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 13574086
#
# ASCII decay Descriptor: [B_s0 -> (D_s- -> (phi -> K+ K-) e- anti-nu_e) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 13574086
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_Dsmunu,phienu=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalRepeatedHadronization.HighVisMass
tightCut.Decay   = '[^(B_s0 => ^(D_s- => ^(phi(1020) => ^K+ ^K-) ^e- ^nu_e~) ^mu+ ^nu_mu)]CC'
tightCut.Cuts    =    {
    '[K+]cc'     : "inAcc",
    '[pi-]cc'    : "inAcc",
    '[e-]cc'     : "inAcc",
    '[mu+]cc'     : "inAcc",
    '[B_s0]cc'     : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'e-' == GID , 'mu+' == GID, 'K+' == GID, 'K-' == GID ) ) > 4500 * MeV ) " ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 531
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/HighVisMass"

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
pgun.EventType = 13574086
