# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15104010.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 15104010
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ pi- K- pi+]cc
#
from Configurables import Generation
Generation().EventType = 15104010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ppiKpi,phsp=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
