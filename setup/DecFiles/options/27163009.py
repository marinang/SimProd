# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163009.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 27163009
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> K- pi+) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27163009
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/DstD0piKpiplus3piFromBIncl=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2dst3piFilter"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2dst3piFilter" )
SignalFilter = Generation().b2dst3piFilter
SignalFilter.Code = "has( isB2cc ) "
SignalFilter.Preambulo += [
"from GaudiKernel.SystemOfUnits import  MeV"
,"isB2cc = GDECTREE('[(Beauty & LongLived) --> (D*(2010)+ -> (D0 => K- pi+) pi+) pi- pi+  pi-  ...]CC')"
   ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LHCbAcceptance"

from Configurables import LHCbAcceptance
pgun.addTool( LHCbAcceptance )

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
pgun.EventType = 27163009
