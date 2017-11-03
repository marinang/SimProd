# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42163201.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 42163201
#
# ASCII decay Descriptor: pp -> [W+ -> (D_s+ -> K+ K- pi+) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42163201
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_Dsgamma=DecProdCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ParsInAcc"


from Configurables import LoKi__FullGenEventCut                                             
Generation().addTool( LoKi__FullGenEventCut, "ParsInAcc" )                               
ParsInAcc = Generation().ParsInAcc

ParsInAcc.Code = " ( count ( isGoodW ) > 0 ) "

ParsInAcc.Preambulo += [                                                                  
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                     
   , "inCaloAcc   = (in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ))"
   , "inAcc       = (in_range(  0.030 , GTHETA , 0.400 ))"
   , "NGoodpim    = (GINTREE((  (('pi-' == GID) )& (GPT >0.3*GeV) & inAcc)))"
   , "NGoodpip    = (GINTREE((  (('pi+' == GID) )& (GPT >0.3*GeV) & inAcc)))"
   , "NGoodKm     = (GINTREE((  (('K-' == GID) )& (GPT >0.3*GeV) & inAcc)))"
   , "NGoodKp     = (GINTREE((  (('K+' == GID) )& (GPT >0.3*GeV) & inAcc)))" 
   , "NGoodKKPip  = (NGoodpip & NGoodKm & NGoodKp)"
   , "NGoodKKPim  = (NGoodpim & NGoodKm & NGoodKp)"
   , "NGoodDs     = (NGoodKKPip | NGoodKKPim)"
   , "NGoodGamma = GINTREE(('gamma' == GABSID) & (GPT >10.0*GeV) & inCaloAcc)"
   , "isGoodW     = ((  'W+' == GABSID ) & NGoodDs & NGoodGamma)" 
   ]

Generation().DecayTool = ""
Generation().Special.DecayTool = ""

from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [
"SpaceShower:rapidityOrder = off", 
"WeakSingleBoson:ffbar2W = on",
"24:addChannel = 1 1. 101 431 22", 
"24:onMode = off", 
"24:onIfAny = 431", 
"431:addChannel = 1 1. 101 321 -321 211",
"431:onMode = off",
"431:onIfMatch = 321 -321 211",
                                       ]


