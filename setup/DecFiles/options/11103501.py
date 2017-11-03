# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11103501.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11103501
#
# ASCII decay Descriptor: {[B0-> (rho+ -> pi+ pi0) (K*(892)- -> (KS0 -> pi+ pi-) pi-)]cc, [B0-> (rho- -> pi- pi0) (K*(892)+ -> (KS0 -> pi+ pi-) pi+)]cc}
#
from Configurables import Generation
Generation().EventType = 11103501
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstrho,KSpi,pipi0=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
