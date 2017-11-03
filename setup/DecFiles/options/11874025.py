# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874025.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11874025
#
# ASCII decay Descriptor: {[B0 => (D- => K+ K- pi-) mu+ nu_mu]cc }
#
from Configurables import Generation
Generation().EventType = 11874025
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,KKpi=cocktail,hqet2,mu3hInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "BeautyTomuCharmTo3h"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
