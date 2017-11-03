# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12875402.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 12875402
#
# ASCII decay Descriptor: [B+ => (D~0 -> K+ K- pi+ pi-) anti-nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 12875402
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0munu,KKpipi=cocktail,D0muInAcc,CutsForD0FromB,BRcorr1.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndCutsForDinSLBdecays"
from Configurables import DaughtersInLHCbAndCutsForDinSLBdecays
Generation().SignalRepeatedHadronization.addTool( DaughtersInLHCbAndCutsForDinSLBdecays )
from GaudiKernel import SystemOfUnits
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndCutsForDinSLBdecays.D0DaughtersPtMin = 300*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndCutsForDinSLBdecays.D0DaughtersPMin = 2.0*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndCutsForDinSLBdecays.MuonPtMin = 1.2*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndCutsForDinSLBdecays.MuonPMin = 3.0*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
Generation().SignalRepeatedHadronization.DaughtersInLHCbAndCutsForDinSLBdecays.D0PtMin = 1.8*SystemOfUnits.GeV
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCbAndCutsForDinSLBdecays"

pgun.addTool( Generation().SignalRepeatedHadronization.DaughtersInLHCbAndCutsForDinSLBdecays.clone() )

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
pgun.EventType = 12875402
