# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/41922001.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 41922001
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]) ([W- -> l nu_l]) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WWlnullnul.py" )
from Configurables import Generation
Generation().EventType = 41922001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WW_lnul,lnul.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoLepFromWs"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoLepFromWs" )
tracksInAcc = Generation().TwoLepFromWs
tracksInAcc.Code = " ( ( count ( isGoodWPlusLepton ) > 0 ) & ( count ( isGoodWMinusLepton ) > 0 ) ) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodWPlusLepton  = ( ( 'W+' == GID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 15*GeV ) ) )"
   , "isGoodWMinusLepton  = ( ( 'W-' == GID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 15*GeV ) ) )"
   ]

