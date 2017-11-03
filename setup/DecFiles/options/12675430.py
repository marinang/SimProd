# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12675430.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 12675430
#
# ASCII decay Descriptor: {[ B+ --> nu_mu mu+ (D~0 -> K+ pi-) ... ]cc}
#
from Configurables import Generation
Generation().EventType = 12675430
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Dststmunu,Dst0=CocktailHigher,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D*(2640)0           763      100423  0.0        2.6492   4.70e-24                  D*(2S)0           0   0.5","D*(2640)~0           764     -100423 0.0        2.6492   4.70e-24                  anti-D*(2S)0           0   0.5","D(2S)0              761      100421  0.0        2.579   3.69e-24                   D(2S)0           0   0.5","D(2S)~0              762     -100421  0.0        2.579   3.69e-24                   anti-D(2S)0           0   0.5","D_1(2420)0          165       10423  0.0        2.978   3.50e-24                     D_10       10423        0.5","D_1(2420)~0          169      -10423 0.0        2.978   3.50e-24                     anti-D_10      -10423        0.5","D*_2(2460)0         170         425  0.0        2.737   9.01660175e-24                    D_2*0         425        0.5","D*_2(2460)~0         166        -425 0.0        2.737   9.01660175e-24                   anti-D_2*0        -425        0.5" ]

from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ (Beauty) ==> ^(D~0 -> ^K+ ^pi- {gamma} {gamma} {gamma}) ^mu+ nu_mu {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
 "from LoKiCore.functions import in_range"  ,
 "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
 "piKP     = GCHILD(GP,('K+' == GABSID )) + GCHILD(GP,('pi-' == GABSID ))" ,
 "piKPT     = GCHILD(GPT,('K+' == GABSID )) + GCHILD(GPT,('pi-' == GABSID ))" ,
]
tightCut.Cuts      =    {
'[pi+]cc'   : " in_range( 0.010 , GTHETA , 0.400 )& ( GPT > 700 * MeV )" ,
'[K-]cc'   : " in_range( 0.010 , GTHETA , 0.400 ) & ( GPT > 700 * MeV )" ,
'[mu+]cc'  : " in_range( 0.010 , GTHETA , 0.400 ) & (GP > 2500* MeV) ",
'[D~0]cc'   : "( piKP > 15000 * MeV ) & (piKPT > 2300 * MeV)"
   }


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
pgun.EventType = 12675430
