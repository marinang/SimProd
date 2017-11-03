# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27163402.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 27163402
#
# ASCII decay Descriptor: [D*(2010)+ -> (D0 -> K- pi+ pi0) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27163402
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Dst_D0pi,Kpipi0=CharmForVubCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 413,-413 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay = " [ D*(2010)+ -> ^( D0 --> ^K- ^pi+ pi0 ) ^pi+ ]CC"
tightCut.Preambulo += [
  "from LoKiCore.functions import in_range"  ,
  "from LoKiGen.functions import LoKi" ,
  "from LoKiGen.HepMC import descendants" ,
  "from GaudiKernel.SystemOfUnits import GeV, MeV"  ,
  "KpiP     = GCHILD(GP,('K-' == GABSID )) + GCHILD(GP,('pi+' == GABSID ))" ,
  "KpiPT     = GCHILD(GPT,('K-' == GABSID )) + GCHILD(GPT,('pi+' == GABSID ))" ,
  "piPT    = GNINTREE( ('pi+' == GABSID ) & (GPT > 500 * MeV) , 1)", 
  "KPT    = GNINTREE( ('K-' == GABSID ) & (GPT > 500 * MeV) , 1)",
]
tightCut.Cuts      =    {
 '[pi+]cc'   : "(in_range( 0.010 , GTHETA , 0.400 ))" ,
 '[K-]cc'   : "(in_range( 0.010 , GTHETA , 0.400 ))" ,
 '[D0]cc'   : "( piPT > 0.5 ) & (KPT > 0.5) & (KpiP > 19000 * MeV) & (KpiPT > 2600 * MeV)" 
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
pgun.EventType = 27163402
