# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/60001018.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 60001018
#
# ASCII decay Descriptor: p Ar40[0.0] => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Beam1GasVeLo.py" )
from Configurables import Generation
Generation().EventType = 60001018
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "HijingProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/beamGasVelo,1=Argon.dec"
Generation().MinimumBias.CutTool = ""
from Configurables import HijingProduction
Generation().MinimumBias.addTool( HijingProduction )
Generation().MinimumBias.HijingProduction.Commands += [
 "hijinginit frame LAB",
  "hijinginit targ A",
  "hijinginit beam1",
  "hijinginit iat 40",
  "hijinginit izt 18"
]
from Configurables import FlatZSmearVertex
Generation().addTool( FlatZSmearVertex )
Generation().FlatZSmearVertex.BeamDirection = 1
from Configurables import UniformSmearVertex
Generation().addTool( UniformSmearVertex )
Generation().UniformSmearVertex.BeamDirection = 1
