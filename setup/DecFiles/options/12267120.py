# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12267120.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 12267120
#
# ASCII decay Descriptor: [B+ -> (D~0 -> (KS0 -> pi+ pi-) K+ K-) pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 12267120
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0pipipi_KSKK_TightCut_PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B+ ==> ^(D~0 => ^(KS0 ==> ^pi+ ^pi-) ^K+ ^K-) ^pi+ ^pi- ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GP > 55000 * MeV) & (GPT > 5000 * MeV) & (GTIME > 0.135 * millimeter)',
    'goodD        = (GP > 25000 * MeV) & (GPT > 2500 * MeV)',
    'goodKS       = (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter)',
    'goodDDaugPi  = (GNINTREE ((("K+" == GABSID) | ("pi+" == GABSID)) & (GP > 2000 * MeV) & inAcc, 4) > 3.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 2000 * MeV) & inAcc, 4) > 1.5)',
    'goodBachPia  = (GNINTREE (("pi+" == GABSID) & (GP > 2000 * MeV) & (GPT > 100 * MeV) & inAcc, 4) > 4.5)',
    'goodBachPic  = (GNINTREE (("pi+" == GABSID) & (GP > 2000 * MeV) & (GPT > 300 * MeV) & inAcc, 4) > 1.5)',
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB  & goodBachPia & goodBachPic',
    '[D0]cc'         : 'goodD  & goodDDaugPi',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi',
    '[pi+]cc'        : 'inAcc'
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
pgun.EventType = 12267120
