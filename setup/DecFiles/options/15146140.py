# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15146140.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 15146140
#
# ASCII decay Descriptor: [Lambda_b0 -> (J/psi(1S) -> mu+ mu-) (Xi- -> (Lambda0 -> p  pi-) pi- ) K+ ]cc
#
from Configurables import Generation
Generation().EventType = 15146140
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiXiK,mm=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
