# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13244214.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 13244214
#
# ASCII decay Descriptor: [B_s0 ->  ( [chi_c1(1P) , chi_c2(1P)] -> (J/psi(1S) -> mu+ mu-) gamma ) pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 13244214
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_chicpipi,Jpsig,mm=TightCuts.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 

tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ B_s0  ->  ( Meson -> ^( J/psi(1S) => ^mu+ ^mu-) ^gamma ) ^pi+ ^pi- ]CC'
tightCut.Cuts      =    {
    'gamma'     : ' goodGamma ' ,
    '[mu+]cc'   : ' goodMuon  ' , 
    '[pi+]cc'   : ' goodPion  ' , 
    'J/psi(1S)' : ' goodPsi   ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodMuon  = ( GPT > 500  * MeV ) & ( GP > 6 * GeV )     & inAcc   ' , 
    'goodKaon  = ( GPT > 150  * MeV )                        & inAcc   ' , 
    'goodPion  = ( GPT > 150  * MeV )                        & inAcc   ' , 
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
pgun.EventType = 13244214
