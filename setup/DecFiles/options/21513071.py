# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21513071.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 21513071
#
# ASCII decay Descriptor: [D+ -> pi+ K- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 21513071
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_piKmu+nu_mu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
