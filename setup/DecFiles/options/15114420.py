# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15114420.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 15114420
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ K- mu+ mu- (pi0 -> gamma gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15114420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_pKmumupi0=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
