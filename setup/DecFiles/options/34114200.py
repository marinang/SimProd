# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34114200.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 34114200
#
# ASCII decay Descriptor: K_S0 -> mu+ mu- (pi0 -> e+ e- gamma)
#
from Configurables import Generation
Generation().EventType = 34114200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KS_mumupi0,eegamma.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
