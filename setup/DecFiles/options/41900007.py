# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/41900007.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 41900007
#
# ASCII decay Descriptor: pp => (t => b ...) (t~ => b~ ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Top_ttbar_qqbar.py" )
from Configurables import Generation
Generation().EventType = 41900007
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ttbar_qqbar_1l17GeV.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/OneLepFromTop"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "OneLepFromTop" )
tracksInAcc = Generation().OneLepFromTop
tracksInAcc.Code = " ( ( count ( isGoodBfromT ) > 1 ) & ( count ( isGoodLepton ) > 0 ) ) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodBfromT   = ( (  6 == GABSID ) & GINTREE( GBEAUTY ) )"
   , "isGoodLepton   = ( ( 'W+' == GABSID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 17*GeV ) ) )"
   ]

