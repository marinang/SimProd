# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/27260210.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 27260210
#
# ASCII decay Descriptor: This is the decay file for the background study for D*+ -> D0(D0->K- pi+ pi- pi+) pi+
#
from Configurables import Generation
Generation().EventType = 27260210
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Dst0.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]
