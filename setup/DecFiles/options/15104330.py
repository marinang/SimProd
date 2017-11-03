# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104330.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 15104330
#
# ASCII decay Descriptor: [Lambda_b0 -> pi+ pi- (Sigma0 -> (Lambda0 -> p+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15104330
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Sigma0pipi,Lambdag,ppi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
