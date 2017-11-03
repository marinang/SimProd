# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165057.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14165057
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> K+ K- pi+) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 14165057
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_PhiDs,KK,KKpi=DDalitz,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
