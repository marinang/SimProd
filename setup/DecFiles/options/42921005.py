# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42921005.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 42921005
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]cc) (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WZlnulbb.py" )
from Configurables import Generation
Generation().EventType = 42921005
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WZ_lnul,bb=1l,5Gev,1b,LoKi.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsTypeCut"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HiggsTypeCut" )
tracksInAcc = Generation().HiggsTypeCut
tracksInAcc.Code = " ( (count ( isGoodBZ ) > 0) & (count ( isGoodLeptonW ) > 0 ) ) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodBZ    = ((  'Z0' == GABSID ) & (GNINTREE( GBEAUTY & ( GTHETA < 400.0*mrad )) > 1))"
   , "isGoodLeptonW   = ((  'W+' == GABSID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & (GPT > 5*GeV)))"
   ]

