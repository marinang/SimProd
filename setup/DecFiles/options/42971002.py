# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42971002.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 42971002
#
# ASCII decay Descriptor: pp -> [W+ -> mu+ nu_mu]cc +b-jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wmunubjet.py" )
from Configurables import Generation
Generation().EventType = 42971002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_munubjet=TightCuts.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsTypeCut"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HiggsTypeCut" )
tracksInAcc = Generation().HiggsTypeCut
tracksInAcc.Code = " ((count ( isGoodLeptonW ) >0) & (count ( isGoodBeauty)>0)) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
    , "isGoodLeptonW     = ((  'W+' == GABSID ) & GINTREE( GLEPTON & ( GTHETA < 400.0*mrad ) & (GPT > 4*GeV)))"
   , "isGoodBeauty   = ((  'b' == GABSID ) & GINTREE( GBEAUTY & ( GTHETA < 400.0*mrad ) & (GPT > 0*GeV)))"
   ]

