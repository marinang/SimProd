# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17164451.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 17164451
#
# ASCII decay Descriptor: [B*_s00 -> ([B_s0]nos -> (D_s- -> K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 17164451
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs00st_Bspi0,Dspi,KKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_s1(L)0 211 10533 0.0 5.7070000 0.658000e-021 B_s10 10533 0.005000", "B_s1(L)~0 215 -10533 0.0 5.7070000 0.658000e-021 anti-B_s10 -10533 0.005000" ]
