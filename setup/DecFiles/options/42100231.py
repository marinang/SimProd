# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42100231.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 42100231
#
# ASCII decay Descriptor: pp -> (Z -> pi0 pi0) ...
#
from Configurables import Generation
Generation().EventType = 42100231
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_pipi=DecProdCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ParsInAcc"

Generation().PileUpTool = "FixedLuminosityForRareProcess"

from Configurables import LoKi__FullGenEventCut 
Generation().addTool(LoKi__FullGenEventCut, "ParsInAcc") 
ParsInAcc = Generation().ParsInAcc

ParsInAcc.Code = " (count(isGoodZ) > 0)"

ParsInAcc.Preambulo += [
    "from GaudiKernel.SystemOfUnits import millimeter, micrometer, MeV, GeV"
  , "inCaloAcc  = (in_range(0.030, abs(GPX/GPZ), 0.300) & in_range(0.030, abs(GPY/GPZ), 0.250) & (GPZ > 0))"
  , "NGoodpi    = (GNINTREE(( (('pi0' == GABSID)) & (GPT > 10.0*GeV) & inCaloAcc)))"
  , "NDausN     = (GNINTREE(GNEUTRAL))"
  , "isGoodZ    = (('Z0' == GABSID) & (NGoodpi == 2) & (NDausN == 2))" 
   ]

# Pythia8 options.
from Gaudi.Configuration import importOptions
from Configurables import Pythia8Production
importOptions('$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py')
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    'WeakSingleBoson:ffbar2gmZ = on',
    'WeakZ0:gmZmode = 2',
    '23:mayDecay = false']


