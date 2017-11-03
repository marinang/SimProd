# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17166052.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 17166052
#
# ASCII decay Descriptor: [B_s1(L)0 -> ([B_s0]nos -> (D_s- -> K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) pi+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 17166052
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_Bspipi,Dspi,KKpi=DDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
