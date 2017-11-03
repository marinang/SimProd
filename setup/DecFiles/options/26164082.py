# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26164082.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 26164082
#
# ASCII decay Descriptor: [Xi_c0 -> [Xi_c+ -> p+ K- pi+] K- ]cc
#
from Configurables import Generation
Generation().EventType = 26164082
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegacstst_XicK,pKpi=phsp,TightCut,m=3067MeV,G=2MeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4132,-4132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_c0               106        4132  0.0        3.0670   0.329000e-021                    Xi_c0        4132   0.010", "Xi_c~0              107       -4132  0.0        3.0670   0.329000e-021              anti-Xi_c0       -4132   0.010" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '[Xi_c0 => ^(Xi_c+ ==> ^p+ ^K- ^pi+) ^K-]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity () ## to be sure ' , 
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack    =  ( GPT > 220 * MeV ) & ( GP  > 3.0 * GeV )   ' , 
    'goodTrack    =  inAcc & inEta                               ' ,     
    'longLived    =  75 * micrometer < GTIME                     ' , 
    'inY          =  in_range ( 1.9   , GY     , 4.6   )         ' , 
    'goodXic      =  inY & longLived     & ( GPT > 0.9 * GeV )   ' ,
]
tightCut.Cuts     =    {
    '[Xi_c+]cc'      : 'goodXic   ' ,
    '[K+]cc'         : 'goodTrack ' , 
    '[pi+]cc'        : 'goodTrack & fastTrack' , 
    '[p+]cc'         : 'goodTrack & fastTrack & ( GP > 9 * GeV ) '
    }

