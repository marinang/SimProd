# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11122400.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11122400
#
# ASCII decay Descriptor: [B0 -> pi0 e+ e-]cc
#
from Configurables import Generation
Generation().EventType = 11122400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_piee=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
