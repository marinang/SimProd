# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/13522021.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 13522021
#
# ASCII decay Descriptor: {[[B_s0] => K- nu_e e+]cc, [B_s~0] => K+ anti-nu_e e+]cc
#
from Configurables import Generation
Generation().EventType = 13522021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs_Kenu=TightCut,M4.5GeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 531,-531 ]

from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
tightCut  = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay    = "[B_s0 => K- e+ nu_e]CC"
tightCut.Cuts     = {
   '[B_s0]cc'  : "GINTREE((GABSID == 'K+') & (ACC)) & GINTREE((GABSID == 'e+') & (ACC)) & (BM2 > 20250000 )",
   }
#
tightCut.Preambulo += [
   "BPX2 = (GCHILD(GPX,'K+' == GABSID) + GCHILD(GPX,'e+' == GABSID))**2",
   "BPY2 = (GCHILD(GPY,'K+' == GABSID) + GCHILD(GPY,'e+' == GABSID))**2",
   "BPZ2 = (GCHILD(GPZ,'K+' == GABSID) + GCHILD(GPZ,'e+' == GABSID))**2",
   "BPE2 = (GCHILD(GE ,'K+' == GABSID) + GCHILD(GE, 'e+' == GABSID))**2",
   "BM2  = (BPE2 - BPX2 - BPY2 - BPZ2)" ,
   "ACC  = in_range ( 0.0075, GTHETA, 0.400 )" , 
   ]


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
pgun.EventType = 13522021
