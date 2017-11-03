# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16145136.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 16145136
#
# ASCII decay Descriptor: [Xi_b- -> (Xi- -> (Lambda0 -> p+ pi-) pi-) (psi(2S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 16145136
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_psi2SXi,mm,Lambdapi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
