# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15144500.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 15144500
#
# ASCII decay Descriptor: [Lambda_b0 -> (J/psi(1S) -> mu+ mu-) (Lambda0 -> p  pi-) (eta -> gamma gamma) ]cc
#
from Configurables import Generation
Generation().EventType = 15144500
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiLambdaeta,mm,gg=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
