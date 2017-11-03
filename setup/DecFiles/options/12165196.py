# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12165196.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 12165196
#
# ASCII decay Descriptor: [B+ -> (D~0 -> pi+ pi-) (K*(892)+ -> (Ks -> pi+ pi-) pi+)]cc
#
from Configurables import Generation
Generation().EventType = 12165196
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0Kst+,pipi,KSpi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = ' ^[B+ -> ^(D~0 => ^pi+ ^pi-) ^(K*(892)+ -> ^(KS0 => ^pi+ ^pi-) ^pi+)]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GP > 50000 * MeV) & (GPT > 4500 * MeV) & (GTIME > 0.12 * millimeter)',
    'goodD        = (GP > 20000 * MeV) & (GPT > 2000 * MeV)',
    'goodKS       = (GP > 4500 * MeV) & (GPT > 450 * MeV)',
    'goodDDaugPi  = (GNINTREE (("pi+" == GABSID) & (GP > 1500 * MeV) & inAcc, 4) > 1.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 2000 * MeV) & inAcc, 4) > 1.5)',
    'goodKstDaugPi= (GNINTREE (("pi+"  == GABSID) & (GP > 5500 * MeV) & (GPT > 550 * MeV) & inAcc, 1) > 0.5)'
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB',
    '[D0]cc'         : 'goodD  & goodDDaugPi',
    '[K*(892)+]cc'   : 'goodKstDaugPi',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi'
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
pgun.EventType = 12165196
