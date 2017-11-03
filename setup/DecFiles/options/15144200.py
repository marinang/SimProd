# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15144200.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 15144200
#
# ASCII decay Descriptor: [Lambda_b0 -> ( chi_c1(1P) -> (J/psi -> mu+ mu- ) gamma ) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 15144200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_chic1pK,Jpsig,mm=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
