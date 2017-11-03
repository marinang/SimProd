# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11124059.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11124059
#
# ASCII decay Descriptor: [B0 -> pi+ pi- e+ e-]cc
#
from Configurables import Generation
Generation().EventType = 11124059
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pipiee=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
