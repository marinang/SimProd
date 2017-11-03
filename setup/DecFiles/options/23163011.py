# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23163011.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 23163011
#
# ASCII decay Descriptor: [Ds+ ->  pi+ pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 23163011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_pipipi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
