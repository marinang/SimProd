# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/31523420.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 31523420
#
# ASCII decay Descriptor: [tau- -> pi- (pi0 -> e+ e- gamma) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 31523420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_nupi+pi0,eegamma=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]
