# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13104014.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 13104014
#
# ASCII decay Descriptor: [B_s0 -> (phi(1020) -> K+ K-) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 13104014
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_phiphi=ptLTcuts,CDFAmp.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi__GenCutTool/TotCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]


from Configurables import Generation, SignalRepeatedHadronization, LoKi__GenCutTool
from GaudiKernel.SystemOfUnits import MeV, mm
from Configurables import LoKi__GenCutTool
gen = Generation()

gen.addTool( SignalRepeatedHadronization )
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TotCut' )

TotCut = gen.SignalRepeatedHadronization.TotCut
TotCut.Decay     = '[^(B_s0 -> (phi(1020) => ^K+ ^K-) (phi(1020) => ^K+ ^K-))]CC'
TotCut.Cuts      =    {
    '[B_s0]cc'    : ' ( GTIME > 1.5 * mm) ' ,
    '[K+]cc'    : ' Track_pT ' ,
    '[K-]cc'    : ' Track_pT ' }
TotCut.Preambulo += [
    'AccCut     = in_range ( 0.005 , GTHETA , 0.400 )' ,
    'Track_pT = ( GPT > 400 * MeV ) & AccCut' ]


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 531
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi__GenCutTool/TotCut"

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
pgun.EventType = 13104014
