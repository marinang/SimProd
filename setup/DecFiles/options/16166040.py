# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16166040.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 16166040
#
# ASCII decay Descriptor: [Xi_b0 -> (Sigma_c(2455)++ -> pi+ (Lambda_c+ -> p K- pi+)) K- pi-]cc
#
from Configurables import Generation
Generation().EventType = 16166040
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_SigmacKpi,Lambdacpi,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
