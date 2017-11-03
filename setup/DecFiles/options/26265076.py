# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26265076.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 26265076
#
# ASCII decay Descriptor: [ Lambda_c(2595)+ -> ( Lambda_c+ -> p+ K- pi+) pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 26265076
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lambdac2595,Lc,pKpi=phsp,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 4214,-4214 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c*+  62  4214 1.0 2.59525 2.5359e-022      Sigma_c*+  4214 0.025", "Sigma_c*~- 63 -4214 -1.0 2.59525 2.5359e-022 anti-Sigma_c*- -4214 0.025" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
#signal     = generation.SignalPlain 
signal     = generation.SignalRepeatedHadronization 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '[ Sigma_c*+ ==> ^( Lambda_c+ ==> ^p+ ^K- ^pi+) pi+ pi- ]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity () ## to be sure ' , 
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack    =  ( GPT > 220 * MeV ) & ( GP  > 3.0 * GeV )   ' , 
    'goodTrack    =  inAcc & inEta & fastTrack                   ' ,     
    'longLived    =  75 * micrometer < GTIME                     ' , 
    'inY          =  in_range ( 1.9   , GY     , 4.6   )         ' , 
    'goodLc       =  inY & longLived     & ( GPT > 0.9 * GeV )   ' ,
    'Bancestors   =  GNINTREE ( GBEAUTY , HepMC.ancestors )      ' , 
    'notFromB     =  0 == Bancestors                             ' , 
]
tightCut.Cuts     =    {
   '[Lambda_c+]cc'  : 'goodLc & notFromB ' ,
   '[K+]cc'         : 'goodTrack ' , 
   '[pi+]cc'        : 'goodTrack ' , 
   '[p+]cc'         : 'goodTrack & ( GP > 9 * GeV ) '
    }

# Generator efficiency histos:
tightCut.XAxis = ( "GCHILD(GPT,'Lambda_c+'==GABSID)/GeV" , 1.0 , 20.0 , 38  )
tightCut.YAxis = ( "GCHILD(GY ,'Lambda_c+'==GABSID)   "  , 2.0 ,  4.5 , 10  )


