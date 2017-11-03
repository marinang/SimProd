# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114053.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11114053
#
# ASCII decay Descriptor: [B0 -> mu+ mu- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11114053
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_4mu=Geq01,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_30 101020 36 0.0 0.214 0.66e-022 H_30 36 0.01","H_20 101021 35 0.0 2.500 0.66e-022 H_20 35 0.01" ]
