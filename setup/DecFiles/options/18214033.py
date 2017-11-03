# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18214033.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 18214033
#
# ASCII decay Descriptor: Upsilon(4S) -> ({Upsilon(1S),Upsilon(2S),Upsilon(3S)} -> mu+ mu-) mu+ mu-
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon4S.py" )
from Configurables import Generation
Generation().EventType = 18214033
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xbbbb_Upsilonmumu,mumu=DecProdCut,18.83GeV.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 300553
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Upsilon(4S)   849   300553   0.0  18.83 5.485e-22       Upsilon(4S)       300553   0.000000e+000" ]
