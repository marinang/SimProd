# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15264110.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 15264110
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s- ->KS0 K-) p+]cc
#
from Configurables import Generation
Generation().EventType = 15264110
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dsp_KSK=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
