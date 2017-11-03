# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21513070.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 21513070
#
# ASCII decay Descriptor: [D+ -> pi+ pi- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 21513070
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pipimu+nu_mu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
