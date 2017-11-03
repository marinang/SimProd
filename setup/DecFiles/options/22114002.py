# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22114002.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 22114002
#
# ASCII decay Descriptor: [D0 -> pi+ pi- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22114002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_pipimumu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
