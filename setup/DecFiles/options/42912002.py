# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42912002.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 42912002
#
# ASCII decay Descriptor: pp -> (Z0 -> b b~) (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/ZZbbbb.py" )
from Configurables import Generation
Generation().EventType = 42912002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ZZ_bb,bb.dec"
Generation().Special.CutTool = "LHCbAcceptance"
