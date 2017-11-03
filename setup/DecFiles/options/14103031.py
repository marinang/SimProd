# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103031.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 14103031
#
# ASCII decay Descriptor: [B_c+ -> p+ p~- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103031
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_ppbarpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
