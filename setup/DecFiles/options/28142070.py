# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28142070.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 28142070
#
# ASCII decay Descriptor: psi(3770) -> mu+ mu-
#
from Configurables import Generation
Generation().EventType = 28142070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_psi3770,mm=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 30443 ]
