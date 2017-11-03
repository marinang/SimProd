# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166070.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11166070
#
# ASCII decay Descriptor: [B0 -> Myanti-Lambda_c- p+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 11166070
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Lcpipip,pKpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
