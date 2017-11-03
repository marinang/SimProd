# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23173001.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 23173001
#
# ASCII decay Descriptor: [D_s+ => ( phi(1020) => mu+ mu- ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 23173001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phipi,mm=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
