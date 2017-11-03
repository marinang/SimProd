# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/40911018.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 40911018
#
# ASCII decay Descriptor: pp -> {[W+ -> {mu+ nu_mu, e+ nu_e}]cc, (Z0 -> {mu+ mu-, e+ e-})} (H_10 -> c anti-c)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Higgs_cc.py" )
from Configurables import Generation
Generation().EventType = 40911018
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_cc=mH125GeV,1cl,5GeV,2c.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HiggsTypeCut"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 125.000 9.400e-026 Higgs0 25 0.000e+000" ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "HiggsTypeCut" )
tracksInAcc = Generation().HiggsTypeCut
tracksInAcc.Code = " ( (count ( isGoodHiggs ) > 0) & ((count ( isGoodLeptonW ) + count ( isGoodLeptonZ ))>0)) "
tracksInAcc.Preambulo += [
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"
   , "isGoodHiggs     = ((  'H_10' == GABSID ) & (GNINTREE( GCHARM & ( GTHETA < 400.0*mrad )) > 1))"
   , "isGoodLeptonW   = ((  'W+' == GABSID ) & GINTREE( GLEPTON & GCHARGED & ( GTHETA < 400.0*mrad ) & (GPT > 5*GeV)))"
   , "isGoodLeptonZ   = ((  'Z0' == GABSID ) & GINTREE( GLEPTON & ( GTHETA < 400.0*mrad ) & (GPT > 5*GeV)))"
   ]

