# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114016.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 11114016
#
# ASCII decay Descriptor: [B0 -> K+ mu+ mu- pi-]cc
#
from Configurables import Generation
Generation().EventType = 11114016
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kpimumu,XLL=DecProdCut,NoMinPCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 5000)

