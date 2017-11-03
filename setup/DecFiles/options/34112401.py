# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34112401.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 34112401
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- pi0
#
from Configurables import Generation
Generation().EventType = 34112401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumupi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 310 ]
