# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17166051.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 17166051
#
# ASCII decay Descriptor: [B_s1(L)0 -> (B_s0 -> (D_s- -> K+ K- pi-) pi+ ) pi+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Bstst_Dstst.py" )
from Configurables import Generation
Generation().EventType = 17166051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_Bspipi,Dspi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_s1(L)0 211 10533 0.0 5.8294 0.658e-021 B_s10 10533 0.005", "B_s1(L)~0 215 -10533 0.0 5.8294 0.658e-021 anti-B_s10 -10533 0.005" ]
