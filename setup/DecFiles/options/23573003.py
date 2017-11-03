# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23573003.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 23573003
#
# ASCII decay Descriptor: [Ds+ ->  phi( K+ K-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23573003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_phimunu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
