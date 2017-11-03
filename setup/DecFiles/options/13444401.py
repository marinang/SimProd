# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13444401.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 13444401
#
# ASCII decay Descriptor: [B_s0 ==> (J/psi(1S) => mu+ mu-) K+ K-  ( eta -> gamma gamma ) ]CC
#
from Configurables import Generation
Generation().EventType = 13444401
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_JpsiKKeta,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = ' ^( ( Beauty & Strange ) ==> ^(J/psi(1S) => ^mu+ ^mu-) ^K+ ^K- ( ^( eta -> ^gamma ^gamma ) || ^( eta => ^pi+ ^pi- ^( pi0 -> ^gamma ^gamma ) ) ) ) ' 

tightCut.Cuts      = {
    '[mu+]cc'             : ' goodMuon  ' , 
    '[K+]cc'              : ' goodKaon  ' , 
    '[pi+]cc'             : ' goodPion  ' , 
    'gamma'               : ' goodGamma ' , 
    'eta'                 : ' goodEta   ' , 
    'pi0'                 : ' goodPi0   ' , 
    'J/psi(1S)'           : ' goodPsi   ' , 
    '[B_s0]cc'            : ' goodB     ' 
    }

tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import micrometer                ' , 
    'GY         = LoKi.GenParticles.Rapidity () ## to be 100% sure   ' , 
    'inEcalX    =   abs ( GPX / GPZ ) < 4.5  / 12.5                  ' , 
    'inEcalY    =   abs ( GPY / GPZ ) < 3.5  / 12.5                  ' , 
    'inEcalHole = ( abs ( GPX / GPZ ) < 0.25 / 12.5 ) & ( abs ( GPY / GPZ ) < 0.25 / 12.5 ) ' , 
    'InEcal     = inEcalX & inEcalY & ~inEcalHole                    ' ,
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) & in_range ( 1.8 , GETA , 5.2 )       ' , 
    'inY        = in_range ( 1.9   , GY     , 4.6   )                ' , 
    'longLived  = 75 * micrometer < GTIME                            ' , 
    'goodMuon   = ( GPT > 500  * MeV ) & ( GP > 6.0 * GeV ) & inAcc  ' , 
    'goodKaon   = ( GPT > 150  * MeV ) & ( GP > 2.5 * GeV ) & inAcc  ' , 
    'goodPion   = ( GPT > 150  * MeV ) & ( GP > 2.5 * GeV ) & inAcc  ' , 
    'goodGamma  = ( GPT > 150  * MeV )                      & InEcal ' , 
    'goodEta    = ( GPT > 750  * MeV )                               ' , 
    'goodPi0    = ( GPT > 200  * MeV )                               ' , 
    'goodPsi    =                                             inY    ' ,
    'goodB      = longLived                                 & inY    ' 
    ]



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
pgun.EventType = 13444401
