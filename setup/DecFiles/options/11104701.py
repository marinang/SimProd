# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104701.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 11104701
#
# ASCII decay Descriptor: [B0-> (eta_prime -> pi+ pi- gamma) (K*0->(KS0->pi+pi-) pi0)]cc
#
from Configurables import Generation
Generation().EventType = 11104701
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kstetap,KSpi,pi+pi-g=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
