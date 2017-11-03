# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11204410.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11204410
#
# ASCII decay Descriptor: [ B0 -> (K_1(1270)0 --> K+ pi- pi0) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 11204410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K1phi,Kpipi0=mK1270,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
