# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18212253.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 18212253
#
# ASCII decay Descriptor: chi_b0(3P) -> (Upsilon -> mu+ mu-) gamma
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18212253
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_chib03P,Upsilongamma,mumu=UpsInAcc.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMax = 10.
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 10551
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "chi_b0(1P) 611 10551 0.0 10.5007 0.000000e+000 chi_b0 10551 0.000000e+000" ]
