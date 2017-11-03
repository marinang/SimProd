# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11154131.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11154131
#
# ASCII decay Descriptor: [[B0]cc => (K_1(1270)0 => KS0 pi+ pi-) (J/psi(1S) => e+ e-)]CC
#
from Configurables import Generation
Generation().EventType = 11154131
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSpipiJpsi,ee=DecProdCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
