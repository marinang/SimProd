# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11246011.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11246011
#
# ASCII decay Descriptor: {[B0 -> (J/psi(1S) -> mu+ mu-) pi+ pi+ pi- pi-]cc,[B0 -> (psi(2S) -> (J/psi(1S) -> mu+ mu-) pi+ pi-) pi+ pi-]cc}
#
from Configurables import Generation
Generation().EventType = 11246011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Jpsipipipipi,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
