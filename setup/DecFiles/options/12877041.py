# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12877041.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 12877041
#
# ASCII decay Descriptor: [B- -> (D_10 -> MyD*+ pi-) anti-nu_mu mu-]cc
#
from Configurables import Generation
Generation().EventType = 12877041
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Dstmunu,piKpipi=cocktail,AMPGEN,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# 
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = "[ B- ==> ^( D*(2010)+ -> ^( D0 -> ^K+ ^pi- ^pi- ^pi+ ) ^pi+ {gamma} {gamma} {gamma} {gamma} ) ^mu- [nu_mu]CC {X} {X} {X} {X} {X} ]CC"

tightCut.Preambulo += [
  "from LoKiCore.functions import in_range"  ,
  "from GaudiKernel.SystemOfUnits import GeV, MeV",
  "inAcc = in_range(0.005,GTHETA,0.4)"
 ]

tightCut.Cuts = {
  '[mu+]cc'       : "inAcc & (GPT > 1.00 * GeV) & (GP > 3.0 * GeV )",
  '[pi+]cc'       : "inAcc & (GPT > 0.10 * GeV) ",
  '[K+]cc'        : "inAcc & (GPT > 0.25 * GeV) & (GP > 1.8 * GeV )",
  '[D0]cc'        : "(GPT > 1.6 * GeV) & (GCHILD(GPT,2) > 0.25 * GeV) & (GCHILD(GP,2) > 1.8 * GeV ) & (GCHILD(GPT,3) > 0.25 * GeV) & (GCHILD(GP,3) > 1.8 * GeV ) & (GCHILD(GPT,4) > 0.25 * GeV) & (GCHILD(GP,4) > 1.8 * GeV )",
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
pgun.EventType = 12877041
