# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15198001.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 15198001
#
# ASCII decay Descriptor: [Lambda_b0 -> (K*0 -> K+ pi-) Lambda_c+ D*(2010)-]cc
#
from Configurables import Generation
Generation().EventType = 15198001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDstKst0,pKpi,Kpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
