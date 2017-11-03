# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104401.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 15104401
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K- (eta -> pi+ pi- pi0)]cc
#
from Configurables import Generation
Generation().EventType = 15104401
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKeta,pi+pi-pi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
