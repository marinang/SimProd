# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163072.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 27163072
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> K- pi+) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27163072
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/DstD0piKpiplus3piFromBInclandanotherD=DecProdCut_generator_cuts.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndCutsForDstarD"
from Configurables import DaughtersInLHCbAndCutsForDstarD
Generation().SignalPlain.addTool( DaughtersInLHCbAndCutsForDstarD )
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstarD.D0PtCuts = 1.500*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstarD.DaughtersPtMinCut = 150*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstarD.DaughtersPtMaxCut = 150*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstarD.DaughtersPMinCut = 1.00*SystemOfUnits.GeV
from GaudiKernel import SystemOfUnits
Generation().SignalPlain.DaughtersInLHCbAndCutsForDstarD.SoftPiPtCut = 100*SystemOfUnits.MeV
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCbAndCutsForDstarD"

pgun.addTool( Generation().SignalPlain.DaughtersInLHCbAndCutsForDstarD.clone() )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 413,-413 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_413.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 27163072
