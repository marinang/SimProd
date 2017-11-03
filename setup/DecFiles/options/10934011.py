# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10934011.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 10934011
#
# ASCII decay Descriptor: psi(2S) -> p+ p~- pi+ pi-
#
from Configurables import Generation
Generation().EventType = 10934011
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=psi2S,pppipi,PTcut,InAcc.dec"
Generation().RepeatDecay.Inclusive.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2psi2SFilter"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2psi2SFilter" )
SignalFilter = Generation().b2psi2SFilter
SignalFilter.Code = " has(isB2ccTcuts)"
SignalFilter.Preambulo += [
 "from GaudiKernel.SystemOfUnits import GeV, mrad",
 "inAcc = (in_range(  0.010 , GTHETA , 0.400 ))",
 "isB2cc = ((GDECTREE('(Beauty & LongLived) --> psi(2S) ...')))",
 "frompsi = 0 != GNINTREE('psi(2S)'== GABSID , HepMC.ancestors )",
 "ppcuts = (GINTREE( (('p+' == GID ) & (GPT > 250) & inAcc & frompsi) ) )",
 "pmcuts = (GINTREE( (('p~-' == GID ) & (GPT > 250) & inAcc & frompsi) ) )",
 "pipcuts = (GINTREE( (('pi+' == GID ) & (GPT > 200) & inAcc & frompsi) ) )",
 "pimcuts = (GINTREE( (('pi-' == GID ) & (GPT > 200) & inAcc & frompsi) ) )",
 "isB2ccTcuts = (isB2cc & ppcuts & pmcuts & pipcuts & pimcuts)"
   ]

