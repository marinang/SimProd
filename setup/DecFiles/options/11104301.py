# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104301.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11104301
#
# ASCII decay Descriptor: [B0 -> (eta_prime -> pi+ pi- gamma) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104301
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapKs,pi+pi-g=DecProdCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
