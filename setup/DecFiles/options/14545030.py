# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14545030.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 14545030
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> (J/psi(1S) -> mu+ mu-) (phi(1020) -> K+ K-)) anti-nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 14545030
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bsmunu,Jpsiphi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
