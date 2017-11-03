# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11112200.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11112200
#
# ASCII decay Descriptor: [B_d0 -> gamma mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11112200
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_gammamumu=MNT,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
