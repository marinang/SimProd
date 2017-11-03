# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14133020.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 14133020
#
# ASCII decay Descriptor: [B_c+ -> (chi_c0 -> K+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14133020
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_chic0pi,KK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
