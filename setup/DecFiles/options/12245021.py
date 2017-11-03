# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12245021.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 12245021
#
# ASCII decay Descriptor: {[B+ -> (psi(2S) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+]cc,[B+ -> (X_1(3872) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) K+]cc,[B+ -> (J/psi -> mu+ mu-) (K_1+ -> (K*(892)0 -> K+ pi-) pi+)]cc,[B+ -> (J/psi -> mu+ mu-) (K_1+ -> (K_0*0 -> K+ pi-) pi+)]cc,[B+ -> (J/psi -> mu+ mu-) (K_1+ -> (rho0 -> pi+ pi-) K+)]cc}
#
from Configurables import Generation
Generation().EventType = 12245021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_JpsiKpipi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

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
pgun.EventType = 12245021
