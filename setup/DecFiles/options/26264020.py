# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26264020.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 26264020
#
# ASCII decay Descriptor: [Sigma_c++ -> (Lambda_c+ --> p+ K- pi+) pi+]CC
#
from Configurables import Generation
Generation().EventType = 26264020
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sc++_Lcpi,pKpi=DecProdCut_pCut1000MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 4222,-4222 ]
