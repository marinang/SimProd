# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11122200.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11122200
#
# ASCII decay Descriptor: [B_d0 -> gamma e+ e-]cc
#
from Configurables import Generation
Generation().EventType = 11122200
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_gammaee=MNT,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
