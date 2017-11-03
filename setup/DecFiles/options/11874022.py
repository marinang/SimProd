# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11874022.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 11874022
#
# ASCII decay Descriptor: {[[B0 => (D- => K+ K- pi-) anti-nu_mu mu+]cc }
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DmuInAcc.py" )
from Configurables import Generation
Generation().EventType = 11874022
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dmunu,KKpi=cocktail,hqet,DmuInAcc,BRCorr1.dec"
Generation().SignalRepeatedHadronization.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
