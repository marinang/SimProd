# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27573401.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 27573401
#
# ASCII decay Descriptor: [D*+ -> (D0 -> (K*- -> K- pi0)  mu+ nu_mu) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27573401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,Kstmunu_Kpi0=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalPlain.TightCut
tightCut.Decay     = "^[ D*(2010)+ -> ^( D0 => (K*(892)- -> ^K- pi0) ^mu+ nu_mu) ^pi+ ]CC"
tightCut.Preambulo += [
    'from LoKiCore.functions import in_range',
    'from GaudiKernel.SystemOfUnits import GeV, MeV',
    'inAcc        = (in_range (0.010, GTHETA, 0.400))',
]

tightCut.Cuts      =    {
    '[D*(2010)+]cc'  : 'inAcc',
    '[K-]cc'         : 'inAcc',
    '[mu+]cc'        : 'inAcc',
    '[pi+]cc'        : 'inAcc'
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
pgun.EventType = 27573401
