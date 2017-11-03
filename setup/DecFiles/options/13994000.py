# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13994000.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 13994000
#
# ASCII decay Descriptor: [[B_s0] ==> (D_2*- -> (D~0 -> K+ mu- nu_mu) pi-) (D_s+ -> mu+ nu_mu)]cc
#
from Configurables import Generation
Generation().EventType = 13994000
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_DD,DD=cocktail,D0muTightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay = "[B_s0 ==> ^((Charm) -> ^mu+ nu_mu ... ) ^(D~0 -> ^K+ ^pi-) {X} {X} {X} {X} {X} {X} {X} ]CC"
tightCut.Preambulo += [
"from GaudiKernel.SystemOfUnits import mrad",
"FilterD = GNINTREE (GCHARM, HepMC.parents)",
"FromD   = 1 == FilterD",
"BCut = (GTHETA < 400.0*mrad)"

]
tightCut.Cuts    =    {
'[mu+]cc'     : "FromD",
'[B_s0]cc'	: "BCut"
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
pgun.EventType = 13994000
