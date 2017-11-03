# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14163011.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 14163011
#
# ASCII decay Descriptor: [B_c+ -> (D0 -> K- pi+) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14163011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0pi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
