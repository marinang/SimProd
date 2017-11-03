# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/28136120.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 28136120
#
# ASCII decay Descriptor: h_c -> (Xi- -> (Lambda -> p+ pi-) pi-) (Xi+ -> (Anti-Lambda -> p- pi+) pi+)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/hc.py" )
from Configurables import Generation
Generation().EventType = 28136120
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/hc_XiXi,Lambdapi,ppi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 10443 ]
