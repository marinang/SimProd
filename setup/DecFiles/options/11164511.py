# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164511.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11164511
#
# ASCII decay Descriptor: {[[B0]nos -> (D0 -> K- pi+) (K*(892)~0 -> KS0 pi0)]cc, [[B0]os -> (D~0 -> K+ pi-) (K*(892)0 -> KS0 pi0)]cc}
#
from Configurables import Generation
Generation().EventType = 11164511
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D0Kst0,KSpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
