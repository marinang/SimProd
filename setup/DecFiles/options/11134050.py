# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11134050.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11134050
#
# ASCII decay Descriptor: [B0 -> (chi_c0(1P) -> pi+ pi-) (K*(892)0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11134050
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_chic0Kst,pipi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
