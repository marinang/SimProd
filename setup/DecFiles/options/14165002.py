# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165002.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14165002
#
# ASCII decay Descriptor: [B_c+ -> ([B_s0]nos -> (D_s- -> K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14165002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi+_Dspi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
