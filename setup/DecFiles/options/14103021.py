# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103021.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 14103021
#
# ASCII decay Descriptor: [B_c+ -> (anti-K*0 -> K- pi+) K+]cc
#
from Configurables import Generation
Generation().EventType = 14103021
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_antiKstK,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
