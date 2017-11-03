# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22114001.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 22114001
#
# ASCII decay Descriptor: [D0 -> phi mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22114001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_phimumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
