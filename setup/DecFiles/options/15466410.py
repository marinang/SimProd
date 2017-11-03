# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15466410.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15466410
#
# ASCII decay Descriptor: [Lambda_b0 -> (D*+ -> (D+ --> K- pi+ pi+) pi0, gamma ) p+ pi- pi-]CC
#
from Configurables import Generation
Generation().EventType = 15466410
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dst+ppi-pi-=phsp.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
