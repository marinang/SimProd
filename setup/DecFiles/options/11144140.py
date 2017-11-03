# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144140.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11144140
#
# ASCII decay Descriptor: [[B0]cc => (K_1(1270)0 => KS0 pi+ pi-) (J/psi(1S) => mu+ mu-)]CC
#
from Configurables import Generation
Generation().EventType = 11144140
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_KSpipiJpsi,mumu=DecProdCut,LSFLAT.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
