# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/43900080.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 43900080
#
# ASCII decay Descriptor: pp -> ( H_20 -> ( H_30 -> b anti-b ) ( H_30 -> tau+ tau-) )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HidValleyH.py" )
from Configurables import Generation
Generation().EventType = 43900080
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_bbtautau,mH=125GeV,mA=30GeV,tA=0ps.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BbtautauInWideAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 125.0 9.4e-26 Higgs'0 35 0.0e+00" , "H_30 89 36 0.0 30.0 9.4e-26 A0 36 0.0e+00" ]


# Restriction the decay to bbtautau
Generation().Special.Pythia8Production.Commands += [
  # Narrow the decay: 
  # H_2^0 (35) -> H_3^0 (36)
  "35:onmode = off",
  "35:onIfAll = 36 36",

  # H_3^0 (36) -> b (5), tau (15)
  "36:mMin = 0",
  "36:mMax = 0",
  "36:isResonance = on",
  "36:onMode = off",
  "36:onIfAny = 5 15",
]
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BbtautauInWideAcceptance" )
cut = Generation().BbtautauInWideAcceptance
cut.Code = " count ( isGoodHiggs ) > 0 "
cut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import ns, GeV, mrad",
    "isInWideAcpt   = (  GTHETA < 480.0*mrad )",
    "isGoodB        = ( (GABSID==5 ) & (isInWideAcpt) )",
    "isGoodTau      = ( (GABSID==15) & (isInWideAcpt) )",
    "isGoodA2bb     = ( (GID==36) & (GNINTREE(isGoodB) >= 2) )",
    "isGoodA2tautau = ( (GID==36) & (GNINTREE(isGoodTau) >= 2) )",
    "isGoodHiggs    = ( (GID==35) & (GNINTREE(isGoodA2bb) >= 1) & (GNINTREE(isGoodA2tautau) >= 1) )",
]

