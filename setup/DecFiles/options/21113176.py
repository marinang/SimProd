# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21113176.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 21113176
#
# ASCII decay Descriptor: [D+ -> (KS0 -> pi+ pi-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 21113176
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_Ksmu+nu_mu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
