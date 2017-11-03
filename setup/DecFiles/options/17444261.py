# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17444261.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 17444261
#
# ASCII decay Descriptor: [B*_20 ->  (B+ -> K+ (J/psi(1S) -> mu+ mu-)) K-]cc, [B*_20 ->  (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+) K-]cc, [B*_20 ->  (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ pi- pi+) K-]cc, [B*_20 ->  ( B*+ -> (B+ -> K+ (J/psi(1S) -> mu+ mu- )) gamma ) K-]cc, [B*_20 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ ) gamma ) K-]cc, [B*_20 ->  ( B*+ -> (B+ -> (D~0 -> {K+ pi-, K+ pi- pi+ pi-}) pi+ pi- pi+) gamma ) K-]cc
#
from Configurables import Generation
Generation().EventType = 17444261
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/B2st0_Bstpi,Bupi,JpsiK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 515,-515 ]
