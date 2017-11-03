# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11398400.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11398400
#
# ASCII decay Descriptor: [B0-> (D*- -> ((D- -> K+ pi- pi-) || (D- -> K+ K- pi-)) (pi0 , gammma)) (D*+ -> (D0 -> K- pi- pi+ pi+) pi+)]cc
#
from Configurables import Generation
Generation().EventType = 11398400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-Dst+,D-pi0,D0pi+,K3pi=DDALITZ,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
