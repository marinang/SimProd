# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103052.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14103052
#
# ASCII decay Descriptor: [B_c+ -> (B0 -> pi+ pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103052
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bdpi+,CPVpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
