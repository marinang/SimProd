# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14175004.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 14175004
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> K+ K- pi+) mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 14175004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dsmumu=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
