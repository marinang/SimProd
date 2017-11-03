# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16164212.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 16164212
#
# ASCII decay Descriptor: [Sigma_b0 -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+ ) pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 16164212
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lbstar5912_Lbgamma,Lcpi=LoKiGenCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5212,-5212 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b0   112   5212  0.0  5.912000  1.000000e-019       Sigma_b0   5212  1.000000e-004", " Sigma_b~0  113  -5212  0.0  5.912000  1.000000e-019  anti-Sigma_b0  -5212  1.000000e-004" ]

from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 5000 )
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )

tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[Sigma_b0 -> ( Lambda_b0 -> (Lambda_c+ -> ^p+ ^K- ^pi+ ) ^pi-) ^gamma]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import MeV" ,
    "from LoKiCore.functions import in_range"
]
tightCut.Cuts      =    {
    'gamma'   : "( GPT > 300*MeV ) & ( in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ) ) ",
    '[p+]cc'  : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 150 * MeV ) & ( GP > 1600*MeV ) " ,
    '[K+]cc'  : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 150 * MeV ) & ( GP > 1600*MeV ) " ,
    '[pi+]cc' : " in_range( 0.010 , GTHETA , 0.300 ) & ( GPT > 150 * MeV ) & ( GP > 1600*MeV ) "
}

