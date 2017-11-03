# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11124110.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11124110
#
# ASCII decay Descriptor: [[B0]cc => (K_1(1270)0 => KS0 pi+ pi-) e+ e-]CC
#
from Configurables import Generation
Generation().EventType = 11124110
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSpipiee=DecProdCut,LSFLAT.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
