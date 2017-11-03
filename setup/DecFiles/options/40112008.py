# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40112008.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 40112008
#
# ASCII decay Descriptor: pp -> (H_10 -> mu mu {,gamma} {,gamma}) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Higgsmumu.py" )
from Configurables import Generation
Generation().EventType = 40112008
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_mm=mH125GeV,inAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/TwoMuonsFromHiggsInAcc"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 125.000 9.400e-026 Higgs0 25 0.000e+000" ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "TwoMuonsFromHiggsInAcc" )
muonsInAcc = Generation().TwoMuonsFromHiggsInAcc
muonsInAcc.Code = " count ( isHiggsWithMuonInAcc ) > 0 "
muonsInAcc.Preambulo += [
      "from GaudiKernel.SystemOfUnits import GeV, mrad"
    , "isHiggs           = ( 'H_10' == GID )"
    , "isMuonInAcc   = ( ( GABSID == 13 )  & ( GPT > 1.0*GeV ) & ( GTHETA < 400.0*mrad ) & ( ( GSTATUS == 1 ) | ( GSTATUS == 999 ) ))"
    , "isHiggsWithMuonInAcc = ( isHiggs & ( GNINTREE(  isMuonInAcc , 4 ) > 1 ) )"
    ]

