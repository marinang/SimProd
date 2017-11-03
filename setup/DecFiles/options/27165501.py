# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27165501.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 27165501
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> (KS0 -> pi+ pi-) pi+ pi- pi0) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27165501
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,KSpipipi0=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D*(2010)+ -> ^( D0 => ^( KS0 => ^pi+ ^pi- ) ^pi+ ^pi- ^pi0) ^pi+]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, mrad ',
    'Dstcut = (GTHETA < 400.0 * mrad) & (GPT > 2000 * MeV)',
    'Dstpioncut  = ( GNINTREE( ("pi+" == GABSID ) & (GP > 1000 * MeV) & (GTHETA < 400.0 * mrad) , 1) > 0.5 )',
    'D0pionscut  = ( GNINTREE( ("pi+" == GABSID ) & (GP > 7000 * MeV) & (GPT > 300 * MeV) & (GTHETA < 400.0 * mrad) , 1) > 1.5 )'     
]
tightCut.Cuts      =    {
    '[D*(2010)+]cc' : 'Dstcut & Dstpioncut',
    '[D0]cc'    : 'D0pionscut',
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
pgun.EventType = 27165501
