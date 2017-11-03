# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/49001000.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 49001000
#
# ASCII decay Descriptor: pp => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HardQCD_minbias.py" )
from Configurables import Generation
Generation().EventType = 49001000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias=HardQCD,pt18GeV.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HighPtPiKInAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool(LoKi__FullGenEventCut, 'HighPtPiKInAcc')
cutTool = Generation().HighPtPiKInAcc
cutTool.Code = 'count(HighPtPiKInAcc) > 0'
cutTool.Preambulo += [
   'from GaudiKernel.SystemOfUnits import ns, GeV, mrad',
   'GPT = LoKi.GenParticles.TransverseMomentum()',
   'isPiK = ((GABSID == 211) | (GABSID ==321))',
   'highPT = ((GTHETA < 400.0*mrad) & (GPT > 18*GeV))',
   'HighPtPiKInAcc = ((isPiK) & (highPT))'
   ]

