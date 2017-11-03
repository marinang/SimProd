# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165056.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 14165056
#
# ASCII decay Descriptor: [B_c+ -> (D+ -> pi+ K- pi+) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 14165056
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_PhiD,KK,piKpi=DDalitz,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
