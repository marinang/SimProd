# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14553012.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 14553012
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) -> e+ e-) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14553012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsimunu,ee=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
