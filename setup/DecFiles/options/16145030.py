# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16145030.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 16145030
#
# ASCII decay Descriptor: [Xi_b- -> ( J/psi(1S) -> mu+ mu- ) p+ K- K- ]cc
#
from Configurables import Generation
Generation().EventType = 16145030
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_JpsipKK,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalRepeatedHadronization
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[Xi_b- ==> ^( J/psi(1S) => ^mu+ ^mu- ) ^p+ ^K- ^K-]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity () ## to be sure ' , 
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack    =  ( GPT > 150 * MeV ) & ( GP  > 2.5 * GeV )   ' , 
    'goodTrack    =  inAcc & inEta & fastTrack                   ' ,     
    'longLived    =  75 * micrometer < GTIME                     ' , 
    'inY          =  in_range ( 1.9   , GY     , 4.6   )         ' , 
    'goodXib      =  inY & longLived                             ' ,
]
tightCut.Cuts     =    {
    '[Xi_b-]cc'   : 'goodXib    ' ,
    '[K+]cc'      : 'goodTrack  ' , 
    '[p+]cc'      : 'goodTrack   & ( GP  >   9 * GeV ) ' , 
    '[mu+]cc'     : 'goodTrack   & ( GPT > 500 * MeV ) ' 
    }

# Generator efficiency histos:
tightCut.XAxis = ( "GPT/GeV" , 0.0 , 40.0 , 40  )
tightCut.YAxis = ( "GY     " , 2.0 ,  4.5 , 10  )


