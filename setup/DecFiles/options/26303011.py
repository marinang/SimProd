# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26303011.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 26303011
#
# ASCII decay Descriptor: {[Sigma_c+ -> p+ p+ K-]cc, [Sigma_c+ -> p+ p+ K- pi+ pi-]cc}
#
from Configurables import Generation
Generation().EventType = 26303011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Hc+_ppK=DecProdCut,m=3220MeV,t=0.2ps,PPChange.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c+ 83 4212 1.0 3.220 2.e-13 Sigma_c+ 4212 0." , "Sigma_c~- 84 -4212 -1.0 3.220 2.e-13 anti-Sigma_c- -4212 0." ]

# Generation().SignalPlain.SignalPIDList = [ 4212, -4212 ]
Generation().SignalRepeatedHadronization.SignalPIDList = [ 4212, -4212 ]


