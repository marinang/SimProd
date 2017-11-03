# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15196091.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 15196091
#
# ASCII decay Descriptor: [Lambda_b0 -> (Sigma_c+ -> (Lambda_c+ -> p+ K- pi+) (D~0 -> K+ pi-)) K-]cc
#
from Configurables import Generation
Generation().EventType = 15196091
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_X+K-,LcD0,pKpi,Kpi=hel,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c+  83  4212  1.0  4.450 1.64553e-023      Sigma_c+   4212  0.00000000", "Sigma_c~- 84 -4212 -1.0  4.450 1.64553e-023 anti-Sigma_c-  -4212  0.00000000" ]
