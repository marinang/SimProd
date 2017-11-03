# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16166013.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 16166013
#
# ASCII decay Descriptor: [Sigma_b0 -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+ ) pi-) pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 16166013
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lbstar6150_Lbpipi,Lcpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5212,-5212 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_b0   112  5212  0.0  6.150  9.4030276e-20  Sigma_b0  5212  50",                                                                                                          "Sigma_b~0   113  -5212  0.0  6.150  9.4030276e-20  anti-Sigma_b0  -5212  50" ]
