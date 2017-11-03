# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11314100.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11314100
#
# ASCII decay Descriptor: {[B0 -> K0S e+ mu-]cc,[B0 -> K0S e+ mu-]cc}
#
from Configurables import Generation
Generation().EventType = 11314100
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSemu=PHSP,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
