# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/43900078.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 43900078
#
# ASCII decay Descriptor: pp->(  H_20 -> ( H_30 -> s anti-s ) ( H_30 -> s anti-s) )
#
from Configurables import Generation
Generation().EventType = 43900078
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA,ssss=mH125GeV,mA5GeV,tA10ps,HidValley.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/FourTracksFromHVPionInAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 125.0 1.65e-22 Higgs'0 35 4.0e-03" , "H_30 89 36 0.0  5.0 1.0e-11      A0 36 0.0e+00" ]

from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HidValleyH.py" )

Generation().Special.PythiaProduction.Commands[:0] = [
    "pyinit pdtinput $DECFILESROOT/ppfiles/HiddenValleyHiggses_lightquarks.pdt"
]
Generation().Special.Pythia8Production.Commands += [
    "36:onMode = off"
  , "36:onIfMatch = 3 -3"
]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "FourTracksFromHVPionInAcceptance" )
tracksInAcc = Generation().FourTracksFromHVPionInAcceptance
tracksInAcc.Code = " count ( isGoodDVfromHVPion ) > 0 "
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import ns, GeV, mrad"
    , "isHVPion           = ( 'H_30' == GID )"
    , "isGoodDVDaughter   = ( (~GVEV) & GCHARGED & ( GP > 2.0*GeV ) & ( GTHETA < 400.0*mrad ) )"
    , "isGoodDVfromHVPion = ( isHVPion & ( GNINTREE( isGoodDVDaughter, HepMC.descendants ) > 3 ) )"
    ]

