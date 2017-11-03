# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18112002.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 18112002
#
# ASCII decay Descriptor: {Upsilon(1S),Upsilon(2S),Upsilon(3S)} -> mu+ mu- {,gamma} {,gamma}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18112002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Upsilons,mm=NoCut.dec"
Generation().Special.CutTool = ""
