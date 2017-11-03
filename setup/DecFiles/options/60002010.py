# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/60002010.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 60002010
#
# ASCII decay Descriptor: p Ne20[0.0] => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Beam2GasVeLo.py" )
from Configurables import Generation
Generation().EventType = 60002010
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "HijingProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/beamGasVelo,2=Neon.dec"
Generation().MinimumBias.CutTool = ""
from Configurables import HijingProduction
Generation().MinimumBias.addTool( HijingProduction )
Generation().MinimumBias.HijingProduction.Commands += [
 "hijinginit frame LAB",
  "hijinginit targ A",
  "hijinginit beam2",
  "hijinginit iat 20",
  "hijinginit izt 10"
]
from Configurables import FlatZSmearVertex
Generation().addTool( FlatZSmearVertex )
Generation().FlatZSmearVertex.BeamDirection = -1
from Configurables import UniformSmearVertex
Generation().addTool( UniformSmearVertex )
Generation().UniformSmearVertex.BeamDirection = -1
