# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18104040.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 18104040
#
# ASCII decay Descriptor: chi_c1(1P) -> ( phi(1020) -> K+ K- ) ( phi(1020) -> K+ K- )
#
from Configurables import Generation
Generation().EventType = 18104040
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=chic1,phiphi,KK,InAcc.dec"
Generation().RepeatDecay.Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2Chic1Filter"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2Chic1Filter" )
SignalFilter = Generation().b2Chic1Filter
SignalFilter.Code = " has(isB2cc)"
SignalFilter.Preambulo += [
  "isB2cc = ((GDECTREE('(Beauty & LongLived) --> chi_c1(1P) ...')))"
   ]

