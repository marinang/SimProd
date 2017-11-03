# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/45000030.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 45000030
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> (u, d, s, c, b) + jet ... )
#
from Configurables import Generation
Generation().EventType = 45000030
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KaplanNeutralino,mN=98GeV,tN=10ps.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/Kaplan_mk98.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan.py" )
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan_mk98.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHADecayFile = "Kaplan_mk98_10ps.LHdec"
Generation().Special.PythiaProduction.PDecayList = [1000022]
