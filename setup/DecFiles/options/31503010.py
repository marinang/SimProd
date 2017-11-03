# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/31503010.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 31503010
#
# ASCII decay Descriptor: [tau- -> pi- pi+ pi- nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 31503010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_pi-pi+pi-nu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
