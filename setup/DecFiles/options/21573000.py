# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21573000.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 21573000
#
# ASCII decay Descriptor: [D+ -> anti-K*0(K- pi+)  mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 21573000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_Kst0munu.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
