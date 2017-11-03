# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144017.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11144017
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu-) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11144017
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B0_Jpsimumu=ball,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
