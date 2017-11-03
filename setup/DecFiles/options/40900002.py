# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40900002.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 40900002
#
# ASCII decay Descriptor: pp -> (H_10 -> b anti-b) + jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HiggsVBF.py" )
from Configurables import Generation
Generation().EventType = 40900002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/HiggsVBF_bb=mH125GeV,inAcc.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsVBFinAcc"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 125.000 9.400e-026 Higgs0 25 0.000e+000" ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HiggsVBFinAcc" )
tracksInAcc = Generation().HiggsVBFinAcc
tracksInAcc.Code = "( (count ( isGoodBFromH ) > 1) & (count(isGoodJet) > 0))"
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodB = ( ( 'b' == GABSID ) & ( GTHETA < 400.0*mrad ) )"
   , "isFromH  = ( 1 == GNINTREE( 'H_10' == GABSID , 0 ) )"
   , "isGoodBFromH = ( isGoodB & isFromH )"
   , "isGoodJet = ( ( 'u' == GABSID or 'd' == GABSID or 's' == GABSID ) & ( GTHETA < 400.0*mrad ) & (GPT > 10.0*GeV) )" ]

