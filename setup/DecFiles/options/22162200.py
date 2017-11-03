# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/22162200.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 22162200
#
# ASCII decay Descriptor: [D0 -> (phi(1020) -> K+ K-) (gamma)]cc
#
from Configurables import Generation
Generation().EventType = 22162200
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_phigamma,KK.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]
