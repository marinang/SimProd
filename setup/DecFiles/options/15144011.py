# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15144011.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 15144011
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K-) (psi(2S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 15144011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_psi2SpK,mm=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
