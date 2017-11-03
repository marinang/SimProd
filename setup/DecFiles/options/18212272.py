# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18212272.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 18212272
#
# ASCII decay Descriptor: chi_b2(2P) -> (Upsilon -> mu+ mu-) gamma
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18212272
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_chib22P,Upsilongamma,mumu=UpsInAcc.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.UpsilonDaughtersInLHCb.NeutralThetaMax = 10.
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 555
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "chi_b2(1P) 388   555 0.0 10.2686 0.000000e+000 chi_b2   555 0.000000e+000" ]
