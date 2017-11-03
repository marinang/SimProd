# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12112001.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 12112001
#
# ASCII decay Descriptor: [B+ -> K+ (tau- -> TAUOLA) mu+]cc
#
from Configurables import Generation
Generation().EventType = 12112001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Ktaumu,3pipi0=DecProdCut,TightCut,tauola8,phsp.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )

tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[ B+ -> ^([mu+]CC) ([tau- ==> ^pi+ ^pi- ^pi- pi0 nu_tau]CC) ^K+ ]CC'
tightCut.Cuts      =    {
    '[pi-]cc'   : ' goodPion  ' ,
    '[K+]cc'    : ' goodKaon  ' ,
    '[mu+]cc'   : ' goodMuon  ' ,
    '[B+]cc'    : ' goodB  ' }
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import MeV',
    'inAcc = in_range( 0.005, GTHETA, 0.400)',
    'goodMuon  = ( GP  > 2500  * MeV ) & inAcc' ,
    'goodKaon  = ( GPT > 650  * MeV ) & inAcc' ,
    'goodPion  = ( GPT > 220  * MeV ) & inAcc' ,
    'goodB     = ( GPT > 2500  * MeV ) ' ]



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
pgun.EventType = 12112001
