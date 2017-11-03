# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28196070.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 28196070
#
# ASCII decay Descriptor: psi(3770) -> D+(K- pi+ pi+)  D-(K+ pi- pi-)
#
from Configurables import Generation
Generation().EventType = 28196070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/psi3770_D+D-,Kpipi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 30443 ]
