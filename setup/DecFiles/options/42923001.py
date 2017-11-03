# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42923001.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 42923001
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]cc) (Z0 -> l+ l-) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WZlnulll.py" )
from Configurables import Generation
Generation().EventType = 42923001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WZ_lnul,ll.dec"
Generation().Special.CutTool = ""

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoLepFromWandZ" )
tracksInAcc = Generation().TwoLepFromWandZ
tracksInAcc.Code = " ( ( count ( isGoodWLepton ) > 0 ) & ( count ( isGoodZLepton ) > 0 ) ) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodWLepton  = ( ( 'W+' == GABSID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 15*GeV ) ) )"
   , "isGoodZLepton  = ( ( 'Z0' == GABSID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & ( GPT > 15*GeV ) ) )"
   ]

