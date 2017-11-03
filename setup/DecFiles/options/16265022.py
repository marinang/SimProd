# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16265022.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 16265022
#
# ASCII decay Descriptor: [Sigma_b+ -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+ ) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 16265022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sb+_Lbpi,Lcpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5222,-5222 ]
