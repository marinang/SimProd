# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874043.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11874043
#
# ASCII decay Descriptor: {[B0 => (D- => K+ pi- pi-) anti-nu_mu mu+]cc }
#
from Configurables import Generation
Generation().EventType = 11874043
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,Kpipi=cocktail,hqet,LHCbAcceptance.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
