# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21101400.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 21101400
#
# ASCII decay Descriptor: [D- -> pi- ( pi0 -> gamma gamma )]cc
#
from Configurables import Generation
Generation().EventType = 21101400
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pi+pi0,gg=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
