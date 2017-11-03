# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12113445.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 12113445
#
# ASCII decay Descriptor: [B+ -> FLATQ2 (K*+ -> K+ pi0) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 12113445
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Kstmumu,Kpi0=PHSP,flatq2,DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B+ -> ^(K*(892)+ -> ^K+ ^(pi0 => ^gamma ^gamma)) ^mu+ ^mu-]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'inAcc     =  in_range( 0.005 , GTHETA , 0.400 )',
    'goodPi0  = (GPT > 630 * MeV) & inAcc'
]  
tightCut.Cuts     =    {
    '[pi0]cc'          : 'goodPi0',
    '[mu+]cc'          : 'inAcc',
    '[pi+]cc'          : 'inAcc'
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
pgun.EventType = 12113445
