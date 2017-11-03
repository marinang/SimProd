# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25163000.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 25163000
#
# ASCII decay Descriptor: {[ Lambda_c+ -> (D0 -> K- pi+) p+ ]cc}
#
from Configurables import Generation
Generation().EventType = 25163000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc2880,D0p+,Kpi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+ 4122 4122 1.0 2.880 6.582e-023 Lambda_c+ 4122 0.07722797", "Lambda_c~- -4122 -4122 -1.0 2.880 6.582e-023 anti-Lambda_c- -4122 0.07722797", "Lambda_c(2625)+ 104124 104124 1.0 4.880 5.00e-024 Lambda_c(2625)+ 0 1.0e-004", "Lambda_c(2625)~- -104124 -104124 -1.0 4.880 5.00e-024 anti-Lambda_c(2625)- 0 1.0e-004" ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
#
tightCut.Decay    = "^[ Lambda_c+ -> (D0 -> ^K- ^pi+) ^p+ ]CC"
tightCut.Cuts     = {
   '[Lambda_c+]cc' : "in_range ( 0.00 , num/den , 1.00 )",
   '[K-]cc'        : "in_range ( 0.010 , GTHETA , 0.400 )",
   '[pi-]cc'       : "in_range ( 0.010 , GTHETA , 0.400 )",
   '[p+]cc'        : "in_range ( 0.010 , GTHETA , 0.400 )",
   }
#
tightCut.Preambulo += [
   "from LoKiGen.decorators import *",
   "from LoKiCore.functions import *",
   "from LoKiCore.math import sqrt",
   "D_PX   = GCHILD(GPX,'p+' == GABSID)",
   "D_PY   = GCHILD(GPY,'p+' == GABSID)",
   "D_PZ   = GCHILD(GPZ,'p+' == GABSID)",
   "D_E    = GCHILD(GE,'p+' == GABSID)",
   "Q_PX   = GPX",
   "Q_PY   = GPY",
   "Q_PZ   = GPZ",
   "Q_E    = GE",
   "D_M    = sqrt(D_E*D_E - D_PX*D_PX - D_PY*D_PY - D_PZ*D_PZ)",
   "Q_M    = sqrt(Q_E*Q_E - Q_PX*Q_PX - Q_PY*Q_PY - Q_PZ*Q_PZ)",
   "PdotD  = 2.0*Q_E*D_E",
   "PdotQ  = 2.0*Q_E*Q_E",
   "DdotQ  = Q_E*D_E - D_PX*Q_PX - D_PY*Q_PY - D_PZ*Q_PZ",
   "Q2     = Q_M*Q_M",
   "P2     = 4.0*Q_E*Q_E",
   "D2     = D_M*D_M",
   "num    = PdotD*Q2 - PdotQ*DdotQ",
   "den    = sqrt((PdotQ*PdotQ - Q2*P2)*(DdotQ*DdotQ - Q2*D2))",
   ]

