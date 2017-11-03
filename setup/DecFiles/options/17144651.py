# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17144651.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 17144651
#
# ASCII decay Descriptor: [B_s1(H)0 -> (B*_s0 -> (B_s0 -> (J/psi(1S) -> mu+ mu- ) (phi(1020) -> K+ K- )) gamma) (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 17144651
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bsprime1_Bsstpi0,Jpsiphi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_s1(L)0 211 10533 0.0 5.7660000 0.658000e-021 B_s10 10533 0.005000", "B_s1(L)~0 215 -10533 0.0 5.7660000 0.658000e-021 anti-B_s10 -10533 0.005000" ]
