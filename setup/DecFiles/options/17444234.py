# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17444234.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 17444234
#
# ASCII decay Descriptor: [B*_s00 ->  (B+ -> K+ (J/psi(1S) -> mu+ mu- )) K-]cc, [B*_s00 ->  (B+ -> (D~0 -> K+ pi-) pi+ ) K-]cc
#
from Configurables import Generation
Generation().EventType = 17444234
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bstst00_Bpi,JpsiK=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 10513,-10513 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "B_1(L)0  203  10513  0.0  6.18000000  0.6582121e-024  B_10  10513  0.750000", "B_1(L)~0  207  -10513  0.0  6.18000000  0.6582121e-024  anti-B_10  -10513  0.750000" ]
