# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42150000.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 42150000
#
# ASCII decay Descriptor: pp -> (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Z2bb.py" )
from Configurables import Generation
Generation().EventType = 42150000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_bb,2binAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/Zwith2binAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "Zwith2binAcc" )
tracksInAcc = Generation().Zwith2binAcc
tracksInAcc.Code = "count ( isGoodBFromZ ) > 1"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodB = ( ( 'b' == GABSID ) & ( GTHETA < 400.0*mrad ) )"
   , "isFromZ  = ( 1 == GNINTREE( 'Z0' == GABSID , 0 ) )"
   , "isGoodBFromZ = ( isGoodB & isFromZ )" ]

