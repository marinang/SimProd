# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22114010.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 22114010
#
# ASCII decay Descriptor: [D0 -> mu+ mu- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 22114010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_mumumumu=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
