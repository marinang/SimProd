# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21573001.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 21573001
#
# ASCII decay Descriptor: [D+ -> anti-K*0(K- pi+)  mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 21573001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_Kst0munu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
