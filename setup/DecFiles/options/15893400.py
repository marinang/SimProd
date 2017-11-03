# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15893400.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15893400
#
# ASCII decay Descriptor: {[Lambda_b0 -> (Lambda_c+ -> p+ K- pi+) (D- --> pi- pi+ pi- ...) ... ]cc}
#
from Configurables import Generation
Generation().EventType = 15893400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcD-,D-2hhhNneutrals=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool(LoKi__FullGenEventCut, "lb2lc3piFilter")
SignalFilter = Generation().lb2lc3piFilter
SignalFilter.Code = "has(goodLb)"
SignalFilter.Preambulo += [
"from GaudiKernel.SystemOfUnits import  MeV",
"isB2cc = GDECTREE('[(Beauty & LongLived) --> (Lambda_c+ -> (p+ K- pi+) pi- pi+  pi-  ...]CC')",
"inAcc = (0 < GPZ) & (100 * MeV < GPT) & in_range(1.8, GETA, 5.0) & in_range(0.005, GTHETA, 0.400)",
"nPi =  GCOUNT(('pi+' == GABSID) & inAcc, HepMC.descendants)"
"nK  =  GCOUNT(('K-' == GABSID) & inAcc, HepMC.descendants)",
"np  =  GCOUNT(('p+' == GABSID) & inAcc, HepMC.descendants)",
"goodLb = isB2cc & (4 <= nPi) & (1 <= nK) & (1 <= np)",
]

