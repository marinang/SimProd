# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/43900050.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 43900050
#
# ASCII decay Descriptor: pp->(  H_20 -> ( H_30 -> b anti-b ) ( H_30 -> b anti-b) )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HidValleyH.py" )
from Configurables import Generation
Generation().EventType = 43900050
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_AA_bbbb,mH=120GeV,mA=15GeV,tA=0ps.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/FourTracksFromHVPionInAcceptance"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20 88 35 0.0 120.0 9.4e-26 Higgs'0 35 0.0e+00" , "H_30 89 36 0.0  15.0 9.4e-26      A0 36 0.0e+00" ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "FourTracksFromHVPionInAcceptance" )
tracksInAcc = Generation().FourTracksFromHVPionInAcceptance
tracksInAcc.Code = " count ( isGoodDVfromHVPion ) > 0 "
### - LoKi::Constants::InfiniteTime       1.0e+10 ns
### - HepMC::IteratorRange::descendants   4
tracksInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import ns, GeV, mrad"
    , "isHVPion           = ( 'H_30' == GID )"
    , "isGoodDVDaughter   = ( ( GTIME == 1.0e+10*ns ) & GCHARGED & ( GP > 2.0*GeV ) & ( GTHETA < 400.0*mrad ) )"
    , "isGoodDVfromHVPion = ( isHVPion & ( GNINTREE( isGoodDVDaughter, 4 ) > 3 ) )"
    ]

