# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13144203.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 13144203
#
# ASCII decay Descriptor: [B_s0 -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (eta_prime -> rho0 gamma)]cc
#
from Configurables import Generation
Generation().EventType = 13144203
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_Jpsietap,mm,rhog=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = ' Beauty  -> ^( J/psi(1S) => ^mu+ ^mu-)  ^( eta_prime -> ^gamma ( rho(770)0 -> ^pi+ ^pi- ) )'
tightCut.Cuts      =    {
    'eta_prime' : ' goodX0    ' ,
    'gamma'     : ' goodGamma ' ,
    '[mu+]cc'   : ' goodMuon  ' , 
    '[pi+]cc'   : ' goodPion  ' , 
    'J/psi(1S)' : ' goodPsi   ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodX0    =   GPT > 2.25 * GeV                  ' , 
    'goodMuon  = ( GPT > 500  * MeV ) & ( GP > 6 * GeV )     & inAcc   ' , 
    'goodPion  = ( GPT > 100  * MeV )                        & inAcc   ' , 
    'goodGamma = ( 0 < GPZ ) & ( 150 * MeV < GPT ) & inEcalX & inEcalY ' ,
    'goodPsi   = ( GPT > 500  * MeV ) & in_range ( 1.8 , GY , 4.5 )    ' ]



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
pgun.EventType = 13144203
