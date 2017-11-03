# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12165524.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 12165524
#
# ASCII decay Descriptor: [B+ -> (anti-D0 -> ((K*+ -> (K_S0 -> pi+ pi-) pi+) (rho- -> (pi- (pi0 -> gamma gamma))))) pi+]cc
#
from Configurables import Generation
Generation().EventType = 12165524
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0Pi,KstRho,Kspipipi0=TightCut,SVV,HELAMP010.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B+ -> ^(D~0 ==> ^(K*(892)+ -> ^(KS0 ==> ^pi+ ^pi-) ^pi+) ^(rho(770)- -> ^pi- ^(pi0 ==> ^gamma ^gamma))) ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' ,
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' ,
    'goodB        = (GP > 7500 * MeV) & (GPT > 1500 * MeV) & (GTIME > 0.105 * millimeter)',
    'goodD        = (GP > 4000 * MeV) & (GPT > 400 * MeV)',
    'goodKS       = (GNINTREE(("KS0"==GABSID) & (GP >  4000 * MeV) & (GPT >  400 * MeV) & (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter))>0.5)',
    'goodDaugPi  = (GNINTREE (("pi+" == GABSID) & (GP > 750 * MeV) & inAcc, 1) > 0.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 500 * MeV) & inAcc, 1) > 1.5)',
    'goodBachPi   = (GNINTREE (("pi+" == GABSID) & (GP > 5000 * MeV) & (GPT > 500 * MeV) & inAcc, 1) > 0.5)',
    'goodPi0      =  (GNINTREE( ("pi0"==GABSID) & (GP > 750 * MeV) & (GPT > 300 * MeV) & inAcc, 1) > 0.5)',
   'goodPi0Gamma = (GNINTREE( ("gamma"==GABSID) & (GP > 750 * MeV) & (GPT > 400 * MeV) & inEcalX  & inEcalY  & inAcc, 1) > 1.5)'
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB  & goodBachPi',
    '[D0]cc'         : 'goodD',
    '[rho(770)-]cc'   :   'goodDaugPi  & goodPi0',
    '[K*(892)+]cc'   :   'goodDaugPi  & goodKS',
    '[KS0]cc'        : 'goodKsDaugPi',
    '[pi0]cc'        : 'goodPi0Gamma'
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
pgun.EventType = 12165524
