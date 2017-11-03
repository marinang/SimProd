# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28102061.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 28102061
#
# ASCII decay Descriptor: eta_c(1S) -> anti-p- p+
#
from Configurables import Generation
Generation().EventType = 28102061
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=etac1S,ppbar,InAcc,PTCut.dec"
Generation().RepeatDecay.Inclusive.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2EtacFilter"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 421, -421, 411, -411, 431, -431, 4122, -4122, 443, 4112, -4112, 4212, -4212, 4222, -4222, 4312, -4312, 4322, -4322, 4332, -4332, 4132, -4132, 4232, -4232, 100443, 441, 10441, 20443, 445, 4214, -4214, 4224, -4224, 4314, -4314, 4324, -4324, 4334, -4334, 4412, -4412, 4414,-4414, 4422, -4422, 4424, -4424, 4432, -4432, 4434, -4434, 4444, -4444, 14122, -14122,  14124, -14124, 100441 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2EtacFilter" )
SignalFilter = Generation().b2EtacFilter
SignalFilter.Code = " has(isB2ccTcuts)"
SignalFilter.Preambulo += [
 "from GaudiKernel.SystemOfUnits import GeV, mrad",
 "inAcc = (in_range(  0.010 , GTHETA , 0.400 ))",
 "isB2cc = ((GDECTREE('(Beauty & LongLived) --> eta_c(1S) ...')))",
 "fromEtac = 0 != GNINTREE('eta_c(1S)'== GABSID , HepMC.ancestors )",
 "ppcuts = (GINTREE( (('p+' == GID ) & (GPT > 900) & inAcc & fromEtac) ) )",
 "pmcuts = (GINTREE( (('p~-' == GID ) & (GPT > 900) & inAcc & fromEtac) ) )",
 "isB2ccTcuts = (isB2cc & ppcuts & pmcuts)"
   ]

