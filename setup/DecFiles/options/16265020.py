# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16265020.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 16265020
#
# ASCII decay Descriptor: [Sigma_b+ -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+) pi-) p+]cc
#
from Configurables import Generation
Generation().EventType = 16265020
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib6658_Lbp,pKpi=DecProdCut,PPChange.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5222,-5222 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Sigma_b+   110   5222  1.0  6.658  1.00000e-019       Sigma_b+   5222  1.000000e-004", " Sigma_b~-  111  -5222  -1.0  6.658  1.000000e-019  anti-Sigma_b-  -5222  1.000000e-004" ]
