# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23712020.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 23712020
#
# ASCII decay Descriptor: [D_s+ --> (phi(1020) ==> mu- mu+) ...]CC
#
from Configurables import Generation
Generation().EventType = 23712020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phiX,mumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
