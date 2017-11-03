# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16875034.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 16875034
#
# ASCII decay Descriptor: [Xi_b- -> (Xi_c0 -> p+ K- K- pi+) anti-nu_mu mu-]cc
#
from Configurables import Generation
Generation().EventType = 16875034
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Xic0munu,pKKpi=cocktail,BRcorr.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
