# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26143010.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 26143010
#
# ASCII decay Descriptor: [Sigma_c+ -> (J/psi(1S) -> mu+ mu-) p+]cc
#
from Configurables import Generation
Generation().EventType = 26143010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_X+_Jpsip,mumu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Sigma_c+  83  4212  1.0  4.450 1.64553e-023      Sigma_c+   4212  0.00000000", "Sigma_c~- 84 -4212 -1.0  4.450 1.64553e-023 anti-Sigma_c-  -4212  0.00000000" ]

Generation().SignalPlain.SignalPIDList = [ 4212, -4212 ]

