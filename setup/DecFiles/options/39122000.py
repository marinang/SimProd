# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/39122000.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 39122000
#
# ASCII decay Descriptor: phi(1020) => e+ e-
#
from Configurables import Generation
Generation().EventType = 39122000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_phi,ee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 333 ]
