# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11274030.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11274030
#
# ASCII decay Descriptor: [B0 -> (Lambda_c+ -> p+ K- pi+) mu-]cc
#
from Configurables import Generation
Generation().EventType = 11274030
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Lambdacmu,pKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
