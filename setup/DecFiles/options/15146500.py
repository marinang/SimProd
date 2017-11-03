# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15146500.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 15146500
#
# ASCII decay Descriptor: [Lambda_b0 -> (J/psi(1S) -> mu+ mu-) (Lambda0 -> p  pi-) (eta -> pi+ pi- (pi0 -> gamma gamma) ) ]cc
#
from Configurables import Generation
Generation().EventType = 15146500
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiLambdaeta,mm,3pi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
