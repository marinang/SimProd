# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15146133.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 15146133
#
# ASCII decay Descriptor: [Lambda_b0 ->  (J/psi(1S) -> mu+ mu-) (phi -> K+ K-) (Lambda0 -> p+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 15146133
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiLambdaphi,mm=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
