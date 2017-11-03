# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25103070.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 25103070
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ pi- K+]cc
#
from Configurables import Generation
Generation().EventType = 25103070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_ppiK=phsp,TightCut,AlsoFromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
generation = Generation() 
signal     = generation.SignalPlain 
signal.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut   = signal.TightCut
tightCut.Decay     = '^[Lambda_c+ ==> ^p+ ^pi- ^K+]CC'
tightCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import millimeter, micrometer,MeV,GeV",
    "GY           =  LoKi.GenParticles.Rapidity () ## to be sure " , 
    "inAcc        =  in_range ( 0.005 , GTHETA , 0.400 )         " ,
    "inEta        =  in_range ( 1.75  , GETA   , 5.15 )          " ,
    "fastTrack    =  ( GPT > 200 * MeV ) & ( GP  > 1.0 * GeV )   " , 
    "goodTrack    =  inAcc & inEta & fastTrack                   " ,     
    "inY          =  in_range ( 1.85   , GY     , 4.85   )       " ,
    "dauPT        =  GCHILD(GPT,('p+' == GABSID )) + GCHILD(GPT,('K-' == GABSID )) + GCHILD(GPT,('pi+' == GABSID ))", 
    "goodLc       =  inY & ( dauPT > 3 * GeV ) & ( GPT > 2.5 * GeV ) & ( GP > 20 * GeV )" ,
]
tightCut.Cuts     =    {
    "[Lambda_c+]cc"  : "goodLc" ,
    "[K+]cc"         : "goodTrack" , 
    "[pi+]cc"        : "goodTrack" , 
    "[p+]cc"         : "goodTrack & ( GP > 10 * GeV )"
    }

