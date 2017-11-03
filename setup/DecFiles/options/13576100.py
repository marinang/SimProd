# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13576100.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 13576100
#
# ASCII decay Descriptor: [B_s0 -> (D'_s1- -> (D- -> K+ pi- pi-) (K_S0 -> pi+ pi-)) mu+ nu_mu ]cc
#
from Configurables import Generation
Generation().EventType = 13576100
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_Ds1munu,Ds1=DpKS0,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool,'TightCut')
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[ [B_s0]cc => ^(D_s1(2536)- ==> ^( D- => ^K+ ^pi- ^pi-) ^(KS0 => ^pi+ ^pi-) ) ^mu+ ^nu_mu ]CC'

tightCut.Preambulo += [
  'inAcc        = (in_range(0.005, GTHETA, 0.400))',
  'GVZ = LoKi.GenVertices.PositionZ()',
  'from GaudiKernel.SystemOfUnits import millimeter',
  'goodMu       = (GPT > 700 * MeV)  & (GP > 2.0*GeV) & inAcc',
  'goodK        = (GPT > 300 * MeV)  & (GP > 2.0*GeV) & inAcc',
  'goodpi       = (GPT > 300 * MeV)  & (GP > 2.0*GeV) & inAcc',
  'goodD        = (GPT > 1200 * MeV)',
  'goodB        = (GFAEVX(abs(GVZ), 0) - GFAPVX(abs(GVZ), 0) > .5 * millimeter)'
  ]
tightCut.Cuts = {
   '[B_s0]cc'   : 'goodB',
   '[D-]cc'     : 'goodD',
   '[K+]cc'     : 'goodK',
   '[pi+]cc'    : 'goodpi',
   '[mu+]cc'    : 'goodMu'
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
pgun.EventType = 13576100
