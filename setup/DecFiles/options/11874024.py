# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874024.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11874024
#
# ASCII decay Descriptor: {[B0 => (D- => K+ K- pi-) mu+ nu_mu]cc }
#
from Configurables import Generation
Generation().EventType = 11874024
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,KKpi=cocktail,hqet2,LHCbAcceptance.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
