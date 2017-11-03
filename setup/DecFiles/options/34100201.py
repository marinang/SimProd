# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34100201.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 34100201
#
# ASCII decay Descriptor: K_S0 -> gamma gamma
#
from Configurables import Generation
Generation().EventType = 34100201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_gammagamma.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
