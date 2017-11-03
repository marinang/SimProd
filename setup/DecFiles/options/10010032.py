# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10010032.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 10010032
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10010032
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=CharmtoKmu,PPTcuts,InAcc.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2Charm2KmuFilterPPTcuts"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2Charm2KmuFilterPPTcuts" )
SignalFilter = Generation().b2Charm2KmuFilterPPTcuts
SignalFilter.Code = " has(isB2Charm2KmuPPTcuts)"
SignalFilter.Preambulo += [
 "from GaudiKernel.SystemOfUnits import  GeV",
 "isB2Charm2KmuRaw = (GBEAUTY & (GDECTREE('[(Beauty & LongLived) -> ([Charm --> K+ mu- ...]CC)  ...]CC')))",
 "isnotmuonfromKL  = ~(GBEAUTY & GDECTREE('[(Beauty & LongLived) --> ([KL0 -> mu+...]CC) ...]CC'))",
 "mucuts = (GINTREE ( (('mu-' == GABSID ) & (GP > 5 * GeV) &  (GPT > 1 * GeV)) ) )",
 "Kcuts = (GINTREE ( ( ('K+' == GABSID ) & (GP > 7 * GeV) & (GPT > 0.3 * GeV)) ) )",
 "isB2Charm2KmuPPTcuts          = ( isB2Charm2KmuRaw  & isnotmuonfromKL & mucuts & Kcuts)"
   ]

