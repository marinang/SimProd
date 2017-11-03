# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114035.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11114035
#
# ASCII decay Descriptor: [B0 -> (A0 -> mu+ mu-)(Higgs'0 -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 11114035
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_PS,4mu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_20  88  35  0.0  4.5     5.0e-12    Higgs'0   35    0.0" , "H_30  89  36  0.0  0.214   5.0e-12    A0        36    0.0" ]
