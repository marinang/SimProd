# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144072.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11144072
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu-) K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 11144072
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_JpsiKK,mm=XLL,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 5000)

