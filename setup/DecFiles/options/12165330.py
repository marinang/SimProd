# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12165330.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 12165330
#
# ASCII decay Descriptor: [B+ -> K+ (anti-D*0 -> (anti-D0 -> (K_S0 -> pi+ pi-) pi+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 12165330
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Dst0K,D0gamma,KSpipi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[B+ => ^(D*(2007)~0 -> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^pi+ ^pi-) ^gamma ) ^K+]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.010, GTHETA, 0.400))',
   'goodB       = (GP > 32500 * MeV) & (GPT > 2000 * MeV) & (GTIME > 0.060 * millimeter)',
   'goodDstar0       = (GP >  20000 * MeV) & (GPT > 2500 * MeV)',
   'goodD0       = (GP >  17500 * MeV) & (GPT > 2000 * MeV)',
   'goodD0Pi  = (GNINTREE( ("pi+"==GABSID) & (GP > 1000 * MeV) & (GPT > 50 * MeV) & inAcc, 1) > 1.5)',
   'goodKSPi  = (GNINTREE( ("pi+"==GABSID) & (GPT >  50 * MeV) & (GP >  1900 * MeV) & inAcc, 1) > 1.5)',
   'goodKS       = (GP >  3500 * MeV) & (GPT > 250 * MeV) ',
   'goodBK = (GNINTREE( ("K+"==GABSID) & (GP > 4500 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)',
   'goodGamma = (GNINTREE( ("gamma"==GABSID) & ( (abs(GPX/GPZ) < 0.315)  &  (abs(GPY/GPZ) < 0.255) & ((abs( GPX/GPZ ) > 0.019)  |  (abs(GPY/GPZ) > 0.019))) , 1) > 0.5)'
]
tightCut.Cuts = {
   '[B+]cc'          : 'goodB & goodBK',
   '[D*(2007)0]cc'   : 'goodDstar0 & goodGamma',
   '[D0]cc'          : 'goodD0 & goodD0Pi',
   '[KS0]cc'         : 'goodKS & goodKSPi',
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
pgun.EventType = 12165330
