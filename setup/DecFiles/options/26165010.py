# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26165010.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 26165010
#
# ASCII decay Descriptor: [ Sigma_c+ -> (D0 -> K- pi+) p+ K- pi+ ]CC
#
from Configurables import Generation
Generation().EventType = 26165010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc+_D0pKpi,Kpi=PPchange,DecProdCut,WithMinPT.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/DaughtersInLHCbAndWithMinPT"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_c+               83        4212   1.0      3.50000000      3.330000e-13                  Sigma_c+        4212      0.00000000", " Sigma_c~-              84       -4212  -1.0      3.50000000      3.330000e-13             anti-Sigma_c-       -4212      0.00000000" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'DaughtersInLHCbAndWithMinPT' )
daughtersInLHCbAndWithMinPT = gen.SignalRepeatedHadronization.DaughtersInLHCbAndWithMinPT
daughtersInLHCbAndWithMinPT.Decay     = '^[ Sigma_c+ -> ^(D0 -> ^K- ^pi+) ^p+ ^K- ^pi+ ]CC'
daughtersInLHCbAndWithMinPT.Preambulo += [
    'from GaudiKernel.SystemOfUnits import MeV ',
    'inAcc     = in_range ( 0.010 , GTHETA , 0.400 ) ',
    'protP     = ( GP > 8000 * MeV )',
    'xiccpT    = ( GPT > 2000 * MeV )'
]
daughtersInLHCbAndWithMinPT.Cuts      =    {
    '[pi+]cc'         : 'inAcc',
    '[K+]cc'          : 'inAcc',
    '[p+]cc'          : 'inAcc & protP',
    '[Sigma_c+]cc'    : 'xiccpT',
    }

Generation().SignalRepeatedHadronization.SignalPIDList = [ 4212, -4212 ]

