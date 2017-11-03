# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15166010.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15166010
#
# ASCII decay Descriptor: [Lambda_b0 -> (D+ --> K- pi+ pi+) p+ pi- pi-]CC
#
from Configurables import Generation
Generation().EventType = 15166010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D+ppi-pi-=phsp.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
