# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12167003.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 12167003
#
# ASCII decay Descriptor: [B+ -> (anti-Sigma_c-- -> (anti-Lambda_c- -> p~- K+ pi- ) pi-) pi+ pi+ p+]cc
#
from Configurables import Generation
Generation().EventType = 12167003
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Sigmacpipip,Lcpi,pKpi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[(B+ => (Sigma_c~-- => (Lambda_c~- ==> p~- K+ pi-) ^pi-) ^pi+ ^pi+ ^p+)]CC'
tightCut.Preambulo += [
    "inAcc        =  in_range ( 0.01 , GTHETA , 0.400 )         "
]
tightCut.Cuts      =    {
    '[pi+]cc'  : 'inAcc',
    '[p+]cc' : 'inAcc'
                        }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12167003
