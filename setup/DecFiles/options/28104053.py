# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28104053.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 28104053
#
# ASCII decay Descriptor: chi_c2(1P) -> ( phi(1020) -> K+ K- ) ( phi(1020) -> K+ K- )
#
from Configurables import Generation
Generation().EventType = 28104053
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_chic2,phiphi=Pt0.3GeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 445 ]
 
from Configurables import LoKi__GenCutTool as GenCutTool 
#
Generation().SignalPlain.addTool( GenCutTool , 'TightCut' ) 
Generation().SignalPlain.TightCut.Decay = "chi_c2(1P) => ^( phi(1020) => ^K+ ^K-) ^( phi(1020) => ^K+ ^K- )"
Generation().SignalPlain.TightCut.Cuts = {
    'K+' : ' ( GPT > 0.3 * GeV ) & inAcc ',
    'K-' : ' ( GPT > 0.3 * GeV ) & inAcc '
    }
Generation().SignalPlain.TightCut.Preambulo += [
    'inAcc   = in_range ( 0.010 , GTHETA , 0.400 ) '
    ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 445
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalPlain.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 445 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_445.root"
pgun.MomentumSpectrum.BinningVariables = "ptpz"
pgun.MomentumSpectrum.HistogramPath = "OutputMomentumSpectrum_ptpz"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 28104053
