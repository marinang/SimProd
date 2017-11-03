# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34112201.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 34112201
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- gamma
#
from Configurables import Generation
Generation().EventType = 34112201
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumugamma.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
