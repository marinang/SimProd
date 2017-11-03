# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12167191.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 12167191
#
# ASCII decay Descriptor: [B- -> (D0 -> (KS0 -> pi+ pi-) pi+ pi-)  (K*(892)- -> (KS0 -> pi+ pi-) pi-)]cc
#
from Configurables import Generation
Generation().EventType = 12167191
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0Kst+,KSpipi,KSpi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B- ==> ^(D0 => ^(KS0 ==> ^pi+ ^pi-) ^pi+ ^pi-) ^(K*(892)-  => ^(KS0 ==> ^pi+ ^pi-) ^pi-)]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GPT > 1500 * MeV) ',
    'goodD0        = (GPT > 500 * MeV)',
    'goodKst        = (GPT > 500 * MeV)',
    'goodKS       = (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter)',
    'goodDDaugPi  = (GNINTREE (("pi+" == GABSID) & (GPT > 100 * MeV) & inAcc, 4) > 1.5)',
   'goodKsPi  = (GNINTREE( ("pi+"==GABSID) & (GPT > 90 * MeV) & inAcc, 1) > 1.5)',
    'goodKstDaugPi = (GNINTREE (("pi+" == GABSID) & (GPT > 100 * MeV) & inAcc, 4) > 0.5)',
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB ',
    '[D0]cc'         : 'goodD0  & goodDDaugPi',
    '[KS0]cc'        : 'goodKS & goodKsPi',
   '[K*(892)-]cc' :  'goodKst & goodKstDaugPi '
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
pgun.EventType = 12167191
