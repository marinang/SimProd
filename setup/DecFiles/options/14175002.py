# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14175002.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 14175002
#
# ASCII decay Descriptor: [B_c+ -> (psi(2S) -> mu+ mu-) (D_s+ -> ( phi(1020) -> K+ K-) pi+ )]cc
#
from Configurables import Generation
Generation().EventType = 14175002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_psi2SDs+,mmKKpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
