# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144110.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 11144110
#
# ASCII decay Descriptor: [B0 -> KS (psi(2S) ->  mu+ mu- {,gamma} {,gamma})]cc
#
from Configurables import Generation
Generation().EventType = 11144110
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SKS,mm=CPV,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
