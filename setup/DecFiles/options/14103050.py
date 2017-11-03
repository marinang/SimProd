# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103050.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 14103050
#
# ASCII decay Descriptor: [B_c+ -> (B0 -> K+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103050
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bdpi+,KK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
