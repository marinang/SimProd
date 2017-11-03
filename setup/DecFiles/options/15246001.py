# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15246001.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15246001
#
# ASCII decay Descriptor: [Lambda_b0 -> ( psi(2S) -> (J/psi -> mu+ mu- ) pi+ pi- ) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15246001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsipipipK=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[Lambda_b0 ==> ^( J/psi(1S) => ^mu+ ^mu- ) ^pi+ ^pi- ^p+ ^K-]CC'
tightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV',
    'GY           =  LoKi.GenParticles.Rapidity () ## to be sure ' , 
    'inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         ' ,
    'inEta        =  in_range ( 1.95  , GETA   , 5.050 )         ' ,
    'fastTrack    =  ( GPT > 180 * MeV ) & ( GP  > 3.0 * GeV )   ' , 
    'goodTrack    =  inAcc & inEta & fastTrack                   ' ,     
    'longLived    =  75 * micrometer < GTIME                     ' , 
    'inY          =  in_range ( 1.9   , GY     , 4.6   )         ' , 
    'goodLb       =  inY & longLived                             ' ,
]
tightCut.Cuts     =    {
    '[Lambda_b0]cc'  : 'goodLb    ' ,
    '[K+]cc'         : 'goodTrack ' , 
    '[pi+]cc'        : 'goodTrack ' , 
    '[p+]cc'         : 'goodTrack & ( GP  >   9 * GeV ) ' , 
    '[mu+]cc'        : 'goodTrack & ( GPT > 500 * MeV ) '
    }

# Generator efficiency histos:
tightCut.XAxis = ( "GPT/GeV" , 1.0 , 20.0 , 38  )
tightCut.YAxis = ( "GY     " , 2.0 ,  4.5 , 10  )


