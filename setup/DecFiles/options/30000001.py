# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/30000001.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 30000001
#
# ASCII decay Descriptor: pp => ?
#
from Configurables import Generation
Generation().EventType = 30000001
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias=Biased5TrkPt600MeV.dec"
Generation().MinimumBias.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/GenTrackPtCut"

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "GenTrackPtCut" )
tracksInAcc = Generation().GenTrackPtCut
tracksInAcc.Code = "(count ( isGoodTrk ) > 4)"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodTrk     = (GCHARGED and (GTHETA < 400.0*mrad) and (GPT > 0.6*GeV) and (GSTATUS == 999 or GSTATUS == 1)  )"
   ]

