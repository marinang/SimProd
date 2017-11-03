# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17146051.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 17146051
#
# ASCII decay Descriptor: [B_s1(L)0 -> (B_s0 -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (phi(1020) -> K+ K-) ) pi+ pi-]
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Bstst_Dstst.py" )
from Configurables import Generation
Generation().EventType = 17146051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_Bspipi,Jpsiphi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_s1(L)0 211 10533 0.0 5.8294 0.658e-021 B_s10 10533 0.005", "B_s1(L)~0 215 -10533 0.0 5.8294 0.658e-021 anti-B_s10 -10533 0.005" ]
