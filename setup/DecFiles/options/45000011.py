# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/45000011.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 45000011
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> (u, d, s, c, b) + jet ... )
#
from Configurables import Generation
Generation().EventType = 45000011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KaplanNeutralino,mN=48GeV,tN=500ps.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/Kaplan_mh114mk48.tbl"]
LHCb__ParticlePropertySvc().Particles = [ "~chi_10  884  1000022  0.0  48.812325  5.000000000000000e-10  unknown  1000022  0.000000e+000" ]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan.py" )
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan_mh114mk48.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHADecayFile = "Kaplan_mh114mk48_500ps.LHdec"
Generation().Special.PythiaProduction.PDecayList = [1000022]
