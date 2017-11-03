# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103401.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14103401
#
# ASCII decay Descriptor: [B_c+ -> K+ pi- pi+ pi0]cc
#
from Configurables import Generation
Generation().EventType = 14103401
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Kpipipi0=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
