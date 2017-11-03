# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28142232.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 28142232
#
# ASCII decay Descriptor: chi_c0 -> ( J/psi -> mu+ mu- ) gamma
#
from Configurables import Generation
Generation().EventType = 28142232
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/chic0_Jpsigamma,mumu=TightCut,LooserCuts.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 10441 ]

from Configurables import LoKi__GenCutTool as GenCutTool
#
Generation().SignalPlain.addTool( GenCutTool , 'TightCut' )
Generation().SignalPlain.TightCut.Decay = "chi_c0(1P) => ^( J/psi(1S) => ^mu+ ^mu-) ^gamma"
Generation().SignalPlain.TightCut.Cuts = {
    '[mu+]cc'   : ' in_range (0.005 , GTHETA , 0.400 )  '
    }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 10441
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalPlain.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 10441 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_10441.root"
pgun.MomentumSpectrum.BinningVariables = "ptpz"
pgun.MomentumSpectrum.HistogramPath = "OutputMomentumSpectrum_ptpz"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 28142232
