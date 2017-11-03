# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103403.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14103403
#
# ASCII decay Descriptor: [B_c+ -> K+ K- K+ pi0]cc
#
from Configurables import Generation
Generation().EventType = 14103403
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_KKKpi0=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
