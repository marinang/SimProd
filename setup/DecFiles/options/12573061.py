# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12573061.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 12573061
#
# ASCII decay Descriptor: [B- -> (D0 -> K- e+ nu_e) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 12573061
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0munu,Kenu=VisibleInAcceptance,HighVisMass.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/HighVisMass"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool(LoKi__GenCutTool ,'HighVisMass')
#
tightCut = gen.SignalRepeatedHadronization.HighVisMass
tightCut.Decay   = '[^(B- => ^(D0 => ^K- ^e+ ^nu_e) ^mu- ^nu_mu~)]CC'
tightCut.Cuts    =    {
    '[K-]cc'     : "inAcc",
    '[e+]cc'     : "inAcc",
    '[mu-]cc'    : "inAcc",
    '[B-]cc'     : "visMass" }
tightCut.Preambulo += [
    "inAcc   = in_range ( 0.005 , GTHETA , 0.400 ) " ,
    "visMass  = ( ( GMASS ( 'e+' == GABSID , 'mu-' == GABSID, 'K-' == GABSID ) ) > 4500 * MeV ) " ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/HighVisMass"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12573061
