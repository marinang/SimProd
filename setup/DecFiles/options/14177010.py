# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14177010.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 14177010
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D0 -> K- pi+ pi- pi+) K+]cc
#
from Configurables import Generation
Generation().EventType = 14177010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiD0K,mmKpipipi=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
