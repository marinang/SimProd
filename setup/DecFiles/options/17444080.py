# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17444080.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 17444080
#
# ASCII decay Descriptor: [B*_s20 ->  (B+ -> K+ (J/psi(1S) -> mu+ mu-)) K-]cc, [B*_s20 ->  (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+) K-]cc, [B*_s20 ->  (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ pi- pi+) K-]cc, [B*_s20 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) K-]cc, [B*_s20 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ ) gamma ) K-]cc, [B*_s20 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ pi- pi+) gamma ) K-]cc
#
from Configurables import Generation
Generation().EventType = 17444080
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs2st_BstK,BuK,JpsiK.dec"
Generation().SignalRepeatedHadronization.CutTool = ""
Generation().SignalRepeatedHadronization.SignalPIDList = [ 535,-535 ]
