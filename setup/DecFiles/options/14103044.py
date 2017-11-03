# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103044.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 14103044
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> pi+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103044
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi+,CPVKpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
