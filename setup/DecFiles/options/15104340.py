# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104340.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 15104340
#
# ASCII decay Descriptor: [Lambda_b0 -> K+ pi- (Sigma0 -> (Lambda0 -> p+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15104340
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Sigma0Kpi,Lambdag,ppi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
