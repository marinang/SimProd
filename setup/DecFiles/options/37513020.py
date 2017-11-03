# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/37513020.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 37513020
#
# ASCII decay Descriptor: [ K+ -> mu+ mu- mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 37513020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/K+_mumumunu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 321,-321 ]
