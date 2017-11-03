# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10002213.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 10002213
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10002213
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=KpigammaX,updated.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BRadiativeCut"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BRadiativeCut" )
radCut = Generation().BRadiativeCut
radCut.Code = " has(myB) "
radCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import  GeV, mrad"
  , "from PartProp.Nodes import LongLived,Beauty"
  , "inCaloAcc   = (in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ))"
  , "inAcc       = (in_range(  0.030 , GTHETA , 0.400 ))"
  , "HighPtNeut  = (((('gamma' == GABSID) | ('pi0' == GABSID) )& (GPT >2.0*GeV) & inCaloAcc))"
  , "NGoodGPi0   = (GINTREE(HighPtNeut))"
  , "NGoodpim    = (GINTREE((  (('pi-' == GID) )& (GPT >0.3*GeV) & inAcc)))"
  , "NGoodpip    = (GINTREE((  (('pi+' == GID) )& (GPT >0.3*GeV) & inAcc)))"
  , "NGoodKm     = (GINTREE((  (('K-' == GID) )& (GPT >0.3*GeV) & inAcc)))"
  , "NGoodKp     = (GINTREE((  (('K+' == GID) )& (GPT >0.3*GeV) & inAcc)))" 
  , "NGoodKpia   = ((NGoodpip)&(NGoodKm))"
  , "NGoodKpib   = ((NGoodpim)&(NGoodKp))"
  , "NGoodKpi    = ( NGoodKpia | NGoodKpib )"
  , "isnotB2Kstg = ((~GDECTREE('[B0 -> (K*(892)0 -> K+ pi-) gamma]CC')))"
  , "isnotB2K1g  = ((~GDECTREE('[B+ -> K_1(1270)+ gamma]CC')))"
  , "isGoodB     = ((GDECTREE('[(Beauty & LongLived) --> K+ pi- ...]CC')))"
  , "myB         = (isGoodB  & NGoodGPi0  &  NGoodKpi & isnotB2Kstg & isnotB2K1g)"
  ]


