# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104164.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11104164
#
# ASCII decay Descriptor: [B0 -> (KS0 -> pi+ pi-) p+ p~-]cc
#
from Configurables import Generation
Generation().EventType = 11104164
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kspp=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
