# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16164411.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 16164411
#
# ASCII decay Descriptor: [Sigma_b0 -> (Lambda_b0 -> (Lambda_c+ -> p+ K- pi+ ) pi-) pi0]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 16164411
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sb0_Lbpi0,Lcpi=DecProdCut_pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5212,-5212 ]
