# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15113001.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 15113001
#
# ASCII decay Descriptor: {[Lambda_b0 -> (tau- -> pi- pi- pi+ nu_tau) mu+ K- p+]cc, [Lambda_b0 -> (tau+ -> pi- pi+ pi+  anti-nu_tau ) mu- K- p+]cc}
#
from Configurables import Generation
Generation().EventType = 15113001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_mutaupK,pipipinu=DecProdCut,tauolababar.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
