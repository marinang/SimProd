# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12147202.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 12147202
#
# ASCII decay Descriptor: [B+ => K+ (psi(2S) => (J/psi(1S) => mu+ mu-) pi+ pi- ) (eta_prime -> (rho(770)0 => pi+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 12147202
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_psi2SetapK,Jpsipipi,mm,rhog,pipi=TightCuts.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ B+  =>  ^K+ ( psi(2S) => ^( J/psi(1S) => ^mu+ ^mu-) ^pi+ ^pi-) ^(eta_prime -> (rho(770)0 => ^pi+ ^pi-) ^gamma) ]CC'
tightCut.Cuts      =    {
    'gamma'               : ' goodGamma ' ,
    '[mu+]cc'             : ' goodMuon  ' , 
    '[K+]cc'              : ' goodKaon  ' , 
    '[pi+]cc'             : ' goodPion  ' ,
    'J/psi(1S) | psi(2S)' : ' goodPsi   ' ,
    'eta_prime'           : ' goodEtap  ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) & in_range(1.8, GETA, 5.2)             ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5                                             ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5                                             ' , 
    'inEcalHole = ( abs ( GPX / GPZ ) < 0.25 / 12.5 ) & ( abs ( GPY / GPZ ) < 0.25 / 12.5 ) ' ,
    'goodMuon  = ( GPT > 490  * MeV ) & ( GP > 5.4 * GeV )             & inAcc              ' , 
    'goodKaon  = ( GPT > 140  * MeV ) & in_range(2.9*GeV, GP, 210*GeV) & inAcc              ' , 
    'goodPion  = ( GPT > 140  * MeV ) & in_range(2.9*GeV, GP, 210*GeV) & inAcc              ' , 
    'goodGamma = ( 0 < GPZ ) & ( 140 * MeV < GPT ) & inEcalX & inEcalY & ~inEcalHole        ' ,
    'goodPsi   = in_range ( 1.8 , GY , 4.5 )                                                ' ,
    'goodEtap  = ( GPT > 340  * MeV )                                                       ']

# Generator efficiency histos:
tightCut.XAxis = ( "GPT/GeV" , 0.0 , 20.0 , 40  )
tightCut.YAxis = ( "GY     " , 2.0 ,  4.5 , 10  )



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
pgun.EventType = 12147202
