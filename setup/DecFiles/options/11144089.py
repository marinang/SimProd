# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144089.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11144089
#
# ASCII decay Descriptor: [B0 -> (psi(2S) -> mu+ mu-) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11144089
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2Smumu,mumu=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
