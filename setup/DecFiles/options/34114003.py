# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34114003.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 34114003
#
# ASCII decay Descriptor: K_S0 -> e+ e- mu+ mu-
#
from Configurables import Generation
Generation().EventType = 34114003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_eemumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 310 ]
