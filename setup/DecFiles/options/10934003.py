# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/10934003.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 10934003
#
# ASCII decay Descriptor: J/psi(1S) -> p+ p~- pi+ pi-
#
from Configurables import Generation
Generation().EventType = 10934003
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=h_c,pppipi,PTcut,InAcc.dec"
Generation().RepeatDecay.Inclusive.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/b2JpsiFilter"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " J/psi(1S)              64         443   0.0      3.52538000      7.085169e-21                     J/psi         443      0.00000000" ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "b2JpsiFilter" )
SignalFilter = Generation().b2JpsiFilter
SignalFilter.Code = " has(isB2ccTcuts)"
SignalFilter.Preambulo += [
 "from GaudiKernel.SystemOfUnits import GeV, mrad",
 "inAcc = (in_range(  0.010 , GTHETA , 0.400 ))",
 "isB2cc = ((GDECTREE('(Beauty & LongLived) --> J/psi(1S) ...')))",
 "fromJpsi = 0 != GNINTREE('J/psi(1S)'== GABSID , HepMC.ancestors )",
 "ppcuts = (GINTREE( (('p+' == GID ) & (GPT > 250) & inAcc & fromJpsi) ) )",
 "pmcuts = (GINTREE( (('p~-' == GID ) & (GPT > 250) & inAcc & fromJpsi) ) )",
 "pipcuts = (GINTREE( (('pi+' == GID ) & (GPT > 200) & inAcc & fromJpsi) ) )",
 "pimcuts = (GINTREE( (('pi-' == GID ) & (GPT > 200) & inAcc & fromJpsi) ) )",
 "isB2ccTcuts = (isB2cc & ppcuts & pmcuts & pipcuts & pimcuts)"
   ]

