# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/17144081.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 17144081
#
# ASCII decay Descriptor: [B*_s20 -> (B+ -> (J/psi(1S) ->  mu+ mu-) K+) K-]cc
#
from Configurables import Generation
Generation().EventType = 17144081
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bs2st_BuK,JpsiK,mm=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 535,-535 ]
