# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15304110.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 15304110
#
# ASCII decay Descriptor: {[Lambda_b0  -> K+ pi- (Lambda0 -> p+ pi-)]cc, [Lambda_b0  -> K- pi+ (Lambda0 -> p+ pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 15304110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LambdaKpi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
