# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12133261.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 12133261
#
# ASCII decay Descriptor: [B+ -> K+ (h_c -> (eta_c -> p+ anti-p-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 12133261
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_hcK,pp=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^([ B+ -> ^K+ ^(h_c(1P) -> ^gamma ^(eta_c(1S) -> ^p+ ^p~-) ) ]CC)'
tightCut.Cuts      =    {
    '[B+]cc'   : ' goodB  ' , 
    '[p+]cc'   : ' goodProton  ' , 
    '[K+]cc'    : ' goodKaon  ' , 
    'gamma'     : ' goodPhoton ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns',
    'from GaudiKernel.PhysicalConstants import c_light',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' ,
    'goodProton  = ( GPT > 250  * MeV ) & inAcc' , 
    'goodKaon  = ( GPT > 150  * MeV )  & inAcc' , 
    'goodPhoton  = ( GPT > 150  * MeV ) & inAcc & inEcalX & inEcalY ' ,
    'goodB  = ( GCTAU > 0.1e-3 * ns * c_light)' ]



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
pgun.EventType = 12133261
