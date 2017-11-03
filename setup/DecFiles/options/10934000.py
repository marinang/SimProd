# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10934000.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 10934000
#
# ASCII decay Descriptor: J/psi(1S) -> p+ p~- pi+ pi-
#
from Configurables import Generation
Generation().EventType = 10934000
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=Jpsi,pppipi,InAcc.dec"
Generation().RepeatDecay.Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2JpsiFilter"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2JpsiFilter" )
SignalFilter = Generation().b2JpsiFilter
SignalFilter.Code = " has(isB2cc)"
SignalFilter.Preambulo += [
 "isB2cc = ((GDECTREE('(Beauty & LongLived) --> J/psi(1S) ...')))"
   ]

