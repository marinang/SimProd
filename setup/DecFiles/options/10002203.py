# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10002203.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 10002203
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10002203
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=KKgammaX,updated.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BRadiativeCut"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BRadiativeCut" )
radCut = Generation().BRadiativeCut
radCut.Code = " has(myB)"
radCut.Preambulo += [
   "from GaudiKernel.SystemOfUnits import  GeV, mrad"
 , "inCaloAcc    = (in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ))"
 , "inAcc        = (in_range(  0.030 , GTHETA , 0.400 ))"
 , "HighPtNeut   = (((('gamma' == GABSID) | ('pi0' == GABSID) )& (GPT >2.0*GeV) & inCaloAcc))"
 , "NGoodGPi0    = (GINTREE(HighPtNeut))"
 , "NGoodKp      = (GINTREE((  (('K-' == GID) )& (GPT >0.3*GeV) & inAcc)))"
 , "NGoodKm      = (GINTREE((  (('K+' == GID) )& (GPT >0.3*GeV) & inAcc)))" 
 , "NGoodKK      = ((NGoodKp)&(NGoodKm))"
 , "isnotB2phig  = ((~GDECTREE('(Beauty & LongLived) -> (phi(1020) -> K+ K-) gamma')))"
 , "isnotB2phiKg = ((~GDECTREE('[B+ -> (phi(1020) -> K+ K-) K+ gamma]CC')))"
 , "isnotB2K1g   = ((~GDECTREE('[B+ -> K_1(1270)+ gamma]CC')))"
 , "isGoodB      = ((GDECTREE('(Beauty & LongLived) --> K+ K- ...')))"
 , "myB          = ( isGoodB  & NGoodGPi0 & NGoodKK & isnotB2phig & isnotB2K1g & isnotB2phiKg )"
   ]

