# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18114051.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 18114051
#
# ASCII decay Descriptor: chi_b0(1P) -> (Upsilon(1S) -> mu+ mu-) (phi(1020) -> K+ K-)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18114051
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xb_Upsilon1Sphi=PPchange,DecProdCut,10.72GeV.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 10551
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " chi_b0(1P)   611   10551   0.0  10.72 0.000000e+000       chi_b0       10551   0.000000e+000" ]
