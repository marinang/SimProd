# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103051.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 14103051
#
# ASCII decay Descriptor: [B_c+ -> (B0 -> K+ K-) K+]cc
#
from Configurables import Generation
Generation().EventType = 14103051
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BdK+,KK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
