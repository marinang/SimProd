# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/41900009.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 41900009
#
# ASCII decay Descriptor: pp => (t => b ...) (t~ => b~ ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Top_ttbar_qqbar_notau.py" )
from Configurables import Generation
Generation().EventType = 41900009
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ttbar_qqbar_2l15GeV.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoLepFromTop"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoLepFromTop" )
tracksInAcc = Generation().TwoLepFromTop
tracksInAcc.Code = " ( ( count ( isGoodWPlusLepton ) > 0 ) & ( count ( isGoodWMinusLepton ) > 0 ) ) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodWPlusLepton  = ( ( 'W+' == GID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 15*GeV ) ) )"
   , "isGoodWMinusLepton  = ( ( 'W-' == GID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 15*GeV ) ) )"
   ]

