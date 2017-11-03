# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/33102101.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 33102101
#
# ASCII decay Descriptor: [Lambda0 -> pi- p+]cc
#
from Configurables import Generation
Generation().EventType = 33102101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lambda_ppi=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3122,-3122 ]
