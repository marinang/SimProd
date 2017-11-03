# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/25102051.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 25102051
#
# ASCII decay Descriptor: [Lambda_c+ -> Sigma- pi+ pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 25102051
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_Sigmapipi=DecProdCut,SameSign.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
