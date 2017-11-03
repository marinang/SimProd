# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14203003.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14203003
#
# ASCII decay Descriptor: [B_c+ -> pi+ pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14203003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_pipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
