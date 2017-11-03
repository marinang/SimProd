# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11166501.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11166501
#
# ASCII decay Descriptor: [B0 -> (D*(2010)- -> (D~0 -> (KS0 -> pi+ pi-) pi+ pi-) pi-) rho(770)+(-> pi+ pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11166501
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-rho+,KSpipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
