# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27105080.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 27105080
#
# ASCII decay Descriptor: [D_s1(2460)+ -> (phi(1020) -> K+ K- ) (phi(1020) -> K+ K- ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 27105080
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2460_phiphipi,KK,KK=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 20433,-20433 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "D_s1(2460)+           172       20433   1.0      2.45950000      6.582100e-22                     D_s1+       20433      0.005", " D_s1(2460)-           176      -20433  -1.0      2.45950000      6.582100e-22                     D_s1-      -20433      0.005" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[D_s1(2460)+ => ^(phi(1020) -> ^K+ ^K- ) ^(phi(1020) -> ^K+ ^K- ) ^pi+]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )               ' ,
    'fastTrack    =  ( GPT > 200 * MeV ) & ( GP  > 1.9 * GeV )         ' , 
    'goodTrack    =  inAcc &  fastTrack                                ' ,     
    'goodDs       =  ( GPT > 0.9 * GeV )         ' ,
    'Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )            ' , 
    'notFromB     =  0 == Bancestors                                   ' 
]

tightCut.Cuts     =    {
    '[D_s1(2460)+]cc': 'goodDs & notFromB ' ,
    '[K+]cc'  : 'goodTrack ' , 
    '[pi+]cc' : 'goodTrack '
    }

