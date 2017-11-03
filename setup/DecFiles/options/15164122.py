# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164122.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15164122
#
# ASCII decay Descriptor: [Lambda_b0 -> (anti-D0 -> K+ K-) (Lambda -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 15164122
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_antiD0Lambda,KKppi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
