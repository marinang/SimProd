# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12145400.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 12145400
#
# ASCII decay Descriptor: [B+ -> (J/psi(1S) -> mu+ mu-) K+ (omega(782) -> pi+ pi- (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 12145400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_KOmegaJpsi,pi0pi+pi-=PHSP,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[ B+ =>  ^(J/psi(1S) => ^mu+ ^mu- )  ^K+ ^(omega(782) => ^pi+ ^pi- ^(pi0 -> ^gamma ^gamma) ) ]CC'
tightCut.Cuts      =    {
    'gamma'     : ' goodGamma ' ,
    '[mu+]cc'   : ' goodMuon  ' ,
    '[K+]cc'    : ' goodKaon  ' ,
    '[pi+]cc'   : ' goodPion  ' ,
    'J/psi(1S)' : ' goodPsi   ' ,
    '[B+]cc'    : ' goodB     ', }
tightCut.Preambulo += [  "GY = LoKi.GenParticles.Rapidity()" ]
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' ,
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' ,
    'goodMuon  = ( GPT > 500  * MeV ) & ( GP > 6 * GeV )     & inAcc   ' ,
    'goodKaon  = ( GPT > 150  * MeV )                        & inAcc   ' ,
    'goodPion  = ( GPT > 150  * MeV )                        & inAcc   ' ,
    'goodGamma = ( 0 < GPZ ) & ( 150 * MeV < GPT ) & inEcalX & inEcalY ' ,
    'goodPsi   = ( GPT > 1000  * MeV ) & in_range( 1.8 , GY , 4.5 )'    ,
    'goodB     = ( GCTAU > 0.1e-3 * ns * c_light ) ', ]



# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

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
pgun.EventType = 12145400
