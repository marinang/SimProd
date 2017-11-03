# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/39112000.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 39112000
#
# ASCII decay Descriptor: [phi(1020) => mu+ mu-]CC
#
from Configurables import Generation
Generation().EventType = 39112000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_phi,mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 333 ]
