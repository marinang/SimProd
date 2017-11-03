# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/32123200.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 32123200
#
# ASCII decay Descriptor: [Sigma+ => p+ (pi0 -> e+ e- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 32123200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sigma+_ppi0,eegamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3222,-3222 ]
