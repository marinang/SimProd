# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34112400.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 34112400
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- pi0
#
from Configurables import Generation
Generation().EventType = 34112400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumupi0.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
