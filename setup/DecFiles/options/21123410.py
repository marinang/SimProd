# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/21123410.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 21123410
#
# ASCII decay Descriptor: [D- -> pi- pi0 (pi0 -> e+ e- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 21123410
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pi+pi0pi0,eeg=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]
