# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16874040.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 16874040
#
# ASCII decay Descriptor: [Xi_b0 => (Xi_c+ -> p K- pi+) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 16874040
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_Xicmunu,pKpi=cocktail.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
