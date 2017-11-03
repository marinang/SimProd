# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12247001.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 12247001
#
# ASCII decay Descriptor: [B+ ==> ( J/psi(1S) => mu+ mu- ) pi+ pi+ pi+ pi- pi-]
#
from Configurables import Generation
Generation().EventType = 12247001
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Jpsi5pi,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ ^( B+ ==> ^( J/psi(1S) => mu+ mu- ) ^pi+ ^pi+ ^pi+ ^pi- ^pi-) ]CC'
tightCut.Cuts      = {
    '[mu+]cc'             : ' goodMuon  ' , 
    '[pi+]cc'             : ' goodPion  ' , 
    'J/psi(1S)'           : ' goodPsi   ' , 
    '[B+]cc'              : ' goodB     ' 
    }

tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import micrometer              ',
    'GY         = LoKi.GenParticles.Rapidity () ## to be 100% sure ', 
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) & in_range ( 1.8 , GETA , 5.2 ) ' , 
    'inY        = in_range ( 1.9   , GY     , 4.6   ) ' , 
    'longLived  = 75 * micrometer < GTIME             ' , 
    'goodMuon   = ( GPT > 500  * MeV ) & ( GP > 6.0 * GeV ) & inAcc ' , 
    'goodPion   = ( GPT > 150  * MeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPsi    =                                             inY   ' ,
    'goodB      = longLived                                 & inY   ' 
    ]



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
pgun.EventType = 12247001
