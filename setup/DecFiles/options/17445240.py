# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17445240.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 17445240
#
# ASCII decay Descriptor: [B_1(L)+ -> ( B*0 -> (B0 -> (K*0 -> K+ pi-) (J/psi(1S) -> mu+ mu- )) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D- -> K+ pi- pi+) pi+) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D- -> K+ pi- pi+) pi+ pi- pi+) gamma ) pi+]cc, [B_1(L)+ -> ( B*0 -> (B0 -> (D*- -> (D~0 -> {K- pi+, K- pi+ pi- pi+}) pi-)  pi+ pi- pi+) gamma ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 17445240
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B1+_Bdstpi,JpsiKst.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10523,-10523 ]
