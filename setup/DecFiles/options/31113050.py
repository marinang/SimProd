# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/31113050.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 31113050
#
# ASCII decay Descriptor: [tau- -> mu+ pi- pi-]cc
#
from Configurables import Generation
Generation().EventType = 31113050
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_mu+pi-pi-=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
