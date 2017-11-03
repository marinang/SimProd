# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/30001129.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 30001129
#
# ASCII decay Descriptor: pp => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/PROQ2O_129.py" )
from Configurables import Generation
Generation().EventType = 30001129
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/minbias_PROQ2O_129.dec"
Generation().MinimumBias.CutTool = ""
