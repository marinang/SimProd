# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26103090.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 26103090
#
# ASCII decay Descriptor: {[Xi_c+ -> p+ K- pi+]cc}
#
from Configurables import Generation
Generation().EventType = 26103090
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic+_pKpi=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 4232,-4232 ]
