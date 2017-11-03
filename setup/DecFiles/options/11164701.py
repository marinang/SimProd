# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164701.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 11164701
#
# ASCII decay Descriptor: [B0 -> (D0 -> (K_S0 -> pi+ pi-) pi0) (eta' -> pi+ pi- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 11164701
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapD0,pi+pi-g,Kspi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
