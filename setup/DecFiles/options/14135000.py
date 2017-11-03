# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14135000.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14135000
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (phi(1020) -> K+ K-)) pi+ {,gamma}]cc
#
from Configurables import Generation
Generation().EventType = 14135000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi+_Jpsiphi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
