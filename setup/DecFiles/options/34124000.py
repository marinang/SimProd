# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34124000.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 34124000
#
# ASCII decay Descriptor: K_S0 -> e+ e- e+ e-
#
from Configurables import Generation
Generation().EventType = 34124000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_4e.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
