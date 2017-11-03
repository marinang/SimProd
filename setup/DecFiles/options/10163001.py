# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10163001.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 10163001
#
# ASCII decay Descriptor: D*(2010)+ -> pi+ (D0 -> K- pi+ )
#
from Configurables import Generation
Generation().EventType = 10163001
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=Dst,piD0,Kpi,plus3pi,InAcc.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2dst3piFilter"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2dst3piFilter" )
SignalFilter = Generation().b2dst3piFilter
SignalFilter.Code = " has(isB2cc)"
SignalFilter.Preambulo += [
 "isB2cc = ((GDECTREE('(Beauty & LongLived) --> D*(2010)+ pi- pi+  pi-  ...')))"
   ]

