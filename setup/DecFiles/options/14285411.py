# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14285411.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 14285411
#
# ASCII decay Descriptor: [B_c+ -> (D_s*+ -> (D_s+ -> K+ K- pi+) pi0) e+ e-]cc
#
from Configurables import Generation
Generation().EventType = 14285411
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dsstee,Kpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
