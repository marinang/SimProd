# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13104093.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 13104093
#
# ASCII decay Descriptor: {[[B_s0]nos -> K+ pi- K- pi+]cc, [[B_s0]os -> K- pi+ K+ pi-]cc}
#
from Configurables import Generation
Generation().EventType = 13104093
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_KpiKpi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]


from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay   = "[^(B_s0 => ^K+ ^pi- ^K- ^pi+)]CC"
tightCut.Cuts    =    {
    '[K+]cc'    : "inAcc",
    '[pi-]cc'   : "inAcc",
    '[B_s0]cc'  : "lowMKpi" }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.010 , GTHETA , 0.400 )' ,
    "lowMKpi   = ( ( GMASS ( 'K+' == GID , 'pi-' == GID ) ) < 2000 * MeV ) & ( ( GMASS ( 'K-' == GID , 'pi+' == GID ) ) < 2000 * MeV )" ]


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
pgun.EventType = 13104093
