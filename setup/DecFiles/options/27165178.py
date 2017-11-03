# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27165178.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 27165178
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> (KS0 -> pi+ pi-) pi+ pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27165178
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,KSpipi=TightCut,For2012.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D*(2010)+ -> ^( D0 -> ^( KS0 -> ^pi+ ^pi- ) ^pi+ ^pi- ) ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter ',
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ',
    'goodD0    = ( GPT > 1300 * MeV) & (GTIME > 0.075 * millimeter) & (GFAEVX( abs( GVZ  ) , 0 )  <  8000.0 * millimeter ) ',
    'pioncuts  = ( GNINTREE( ("pi+" == GABSID ) & (GP > 1300 * MeV) , 1) > 1.5 )',
    'goodDst   = ( (GPT > 1800 * MeV) & (GPT < (3 * GP / 10)) & (GPT > (2 * GP / 100)) ) ',
    'trigger   = ( GNINTREE( ("pi+" == GABSID) & (GPT > 1400 * MeV ) & (GP > 2700 * MeV) , 4)  > 0.5) ',
]
tightCut.Cuts      =    {
    '[pi+]cc'   : 'inAcc',
    '[D0]cc'    : 'goodD0 & pioncuts & trigger',
    '[D*(2010)+]cc' : 'goodDst',
    }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 413
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalPlain.TightCut.clone(), "TightCut" )

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
pgun.EventType = 27165178
