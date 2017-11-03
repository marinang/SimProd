# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11102211.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 11102211
#
# ASCII decay Descriptor: [B0 -> (K*(892)0 -> K+ pi-) pi0 gamma]cc
#
from Configurables import Generation
Generation().EventType = 11102211
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KstPi0gamma,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
