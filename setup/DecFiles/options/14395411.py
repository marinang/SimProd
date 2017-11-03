# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14395411.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 14395411
#
# ASCII decay Descriptor: [B_c+ -> (D*+ -> (D0 -> K- pi+) pi+) (anti-D*0 -> (anti-D0 -> K+ pi-) (pi0, gamma)) ]cc
#
from Configurables import Generation
Generation().EventType = 14395411
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstDst0=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
