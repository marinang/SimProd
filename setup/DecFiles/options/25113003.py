# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25113003.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 25113003
#
# ASCII decay Descriptor: [Lambda_c+ -> mu+ (phi( ->mu+ mu-)) ]cc
#
from Configurables import Generation
Generation().EventType = 25113003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_phip,mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
