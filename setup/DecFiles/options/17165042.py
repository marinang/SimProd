# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17165042.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 17165042
#
# ASCII decay Descriptor: [B_1(L)+ ->  ([B_s0]nos -> (D_s- -> K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 17165042
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/X5568+_Bspi+,Dspi,KKpi=DecProdCut,PPChange,MaxWidth.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10523,-10523 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_1(L)+               195       10523   1.0      5.5680000      2.992000e-23                      B_1+       10523      0.10000000", "B_1(L)-               199      -10523  -1.0      5.5680000      2.992000e-23                      B_1-      -10523      0.10000000" ]
