# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34312000.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 34312000
#
# ASCII decay Descriptor: (K_S0 -> e+ mu-) (K_S0 -> e- mu+)
#
from Configurables import Generation
Generation().EventType = 34312000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_emu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 310 ]
