# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103029.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 25103029
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 25103029
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_pKpi=TightCut,LifeTimePT.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+  62  4122  1.0  2.468 4.400000e-013 Lambda_c+  4122  0","Lambda_c~-  63 -4122 -1.0  2.468 4.400000e-013  anti-Lambda_c-  -4122   0." ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation()
signal     = generation.SignalPlain
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[Lambda_c+ ==>  ^p+ ^K- ^pi+]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity ()               ' ,
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack    =  ( GPT > 300. * MeV ) & ( GP  > 3.0 * GeV )   ' ,
    'goodTrack    =  inAcc & inEta & fastTrack                   ' ,
    'longLived    =  160. * micrometer < GTIME                    ' ,
    'inY          =  in_range ( 1.9   , GY     , 4.6   )         ' ,
    'goodLc       =  inY & longLived     & ( GPT > 3.0 * GeV )   ' ,
    'Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )      ' ,
    'notFromB     =  0 == Bancestors                             ' ,
]
tightCut.Cuts     =    {
    '[Lambda_c+]cc'  : 'goodLc & notFromB ' ,
    '[K+]cc'         : 'goodTrack ' ,
    '[pi+]cc'        : 'goodTrack ' ,
    '[p+]cc'         : 'goodTrack & ( GP > 9. * GeV ) '
    }

