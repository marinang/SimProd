# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13166123.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 13166123
#
# ASCII decay Descriptor: [[([B_s0]nos => ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ^(K*(892)~0  => ^K- ^pi+))]CC, [([B_s0]os  => ^(D0  => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ^(K*(892)0 => ^K+ ^pi-))]CC]
#
from Configurables import Generation
Generation().EventType = 13166123
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_D0Kst,KSKK=B-SVS,D-PHSP,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[Beauty-> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^K-) ^(K*(892)~0 =>^K- ^pi+) ]CC'
tightCut.Preambulo += [
   'GVZ = LoKi.GenVertices.PositionZ()',
   'from GaudiKernel.SystemOfUnits import millimeter',
   'inAcc        = (in_range(0.005, GTHETA, 0.400))',
   'goodB0       = (GP > 50000 * MeV) & (GPT > 5000 * MeV) & (GTIME > 0.105 * millimeter)',
   'goodD0       = (GP > 20000 * MeV) & (GPT >  300 * MeV)',
   'goodKst      = (GP > 12000 * MeV) & (GPT >  800 * MeV)',
   'goodKS       = (GP >  6000 * MeV) & (GFAEVX(abs(GVZ),0) < 2400.0 * millimeter)',
   'goodDDaugK  = (GNINTREE( ("K+"==GABSID) & (GP > 1000 * MeV) & inAcc, 1) > 1.5)',
   'goodKsDaugPi = (GNINTREE( ("pi+"==GABSID) & (GP > 2000 * MeV) & inAcc, 1) > 1.5)',
   'goodKstPi  = (GNINTREE( ("pi+"==GABSID) & (GP > 2000 * MeV) & (GPT > 98 * MeV) & inAcc, 1) > 0.5)',
   'goodKstK   = (GNINTREE( ("K+"==GABSID) & (GP > 2000 * MeV) & (GPT > 98 * MeV) & inAcc, 1) > 0.5)',
]
tightCut.Cuts = {
   'Beauty'          : 'goodB0', 
   '[D0]cc'          : 'goodD0 & goodDDaugK',
   '[K*(892)0]cc'    : 'goodKst & goodKstPi & goodKstK',
   '[KS0]cc'         : 'goodKS & goodKsDaugPi'
   }


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
pgun.EventType = 13166123
