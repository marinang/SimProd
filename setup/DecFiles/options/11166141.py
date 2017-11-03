# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166141.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11166141
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (D~0 -> (KS0 -> pi+ pi-) pi+ pi-) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 11166141
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-pi,KSpipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
