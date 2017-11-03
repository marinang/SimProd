# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/31113014.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 31113014
#
# ASCII decay Descriptor: [tau- -> mu- e+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 31113014
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_mumue=SS,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
