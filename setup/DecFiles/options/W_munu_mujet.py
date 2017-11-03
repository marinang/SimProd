"""

Pythia options for W_munu_mujet 42311012

- Derived from 42311010.
- Ask another muon of PT>4 GeV, in wide acceptance.
- Also with DPHI > 2.5 with muon from W (back-to-back)

"""

from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

## Option for Pythia8
from Configurables import Special, Pythia8Production
Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )
Generation().Special.Pythia8Production.Commands += [
  "SpaceShower:rapidityOrder = off", #pT ordering!
  "WeakBosonAndParton:qqbar2Wg = on", #q qbar -> W g
  "WeakBosonAndParton:qg2Wq = on", #q g -> W q
  "24:onMode = off", #Turn W decay off
  "24:onIfAny = 13 -13" #Turn on mu+, mu- decays
]


## Cut for another muon, not from W
from Configurables import LoKi__FullGenEventCut
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/LoKi__FullGenEventCut"
Generation().addTool( LoKi__FullGenEventCut )
cut = Generation().LoKi__FullGenEventCut
cut.Code = "(count(OtherMu)>=1) & (dphi_mumu>2.5)"
cut.Preambulo += [
  "from GaudiKernel.SystemOfUnits import GeV, mrad",
  "from GaudiKernel.PhysicalConstants import pi",
  'IsW          = (GABSID==24)',
  'IsMuon       = (GABSID==13)',
  'InWideAcpt   = (GTHETA < 480.0*mrad )',
  'CutPT        = (GPT > 4*GeV)',
  'NotFromW     = (~GHAS( IsW, HepMC.ancestors ))',
  #
  'OtherMu    = IsMuon & InWideAcpt & CutPT & NotFromW',
  #
  'muons      = (select(IsMuon & InWideAcpt & CutPT))',
  'dphiraw    = ((muons >> max_value(GPHI)) - (muons >> min_value(GPHI)))',
  'dphi_mumu  = (pi - abs(dphiraw-pi))',
]

