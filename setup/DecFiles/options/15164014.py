# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164014.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15164014
#
# ASCII decay Descriptor: [Lambda_b0 -> (D0 -> K- pi+) p+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 15164014
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_D0ppi,Kpi=PHSP.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
