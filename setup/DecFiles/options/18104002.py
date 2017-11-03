# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18104002.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 18104002
#
# ASCII decay Descriptor: eta_b(1S) -> ( K*(892)0 -> K+ pi- ) ( K*(892)~0 -> K- pi+ )
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18104002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Etab_KstKst,Kpi=DecProdCut.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 553
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Upsilon(1S)           387         553   0.0      9.39800000      0.000000e+00                   Upsilon         553      0.00000000" ]
