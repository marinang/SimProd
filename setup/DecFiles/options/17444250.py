# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17444250.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 17444250
#
# ASCII decay Descriptor: [B_s1(L)0 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) K-]cc, [B_s1(L)0 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ ) gamma ) K-]cc, [B_s1(L)0 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ pi- pi+) gamma ) K-]cc
#
from Configurables import Generation
Generation().EventType = 17444250
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs1_BstK,JpsiK.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10533,-10533 ]
