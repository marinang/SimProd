# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14145018.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14145018
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> (J/psi(1S) -> mu+ mu-) (phi(1020) -> K+ K-)) K+]cc
#
from Configurables import Generation
Generation().EventType = 14145018
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BsK+_Jpsiphi,mm=CPV,update2012,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
