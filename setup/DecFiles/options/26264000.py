# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26264000.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 26264000
#
# ASCII decay Descriptor: [Sigma_c0 -> (Lambda_c+ --> p+ K- pi+) pi-]CC
#
from Configurables import Generation
Generation().EventType = 26264000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sc0_Lcpi,pKpi=DecProdCut_pCut1000MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 4112,-4112 ]
