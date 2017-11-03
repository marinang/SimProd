# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28194070.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 28194070
#
# ASCII decay Descriptor: psi(3770) -> D0(K- pi+)  D0bar(K+ pi-)
#
from Configurables import Generation
Generation().EventType = 28194070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/psi3770_D0D0bar,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 30443 ]
