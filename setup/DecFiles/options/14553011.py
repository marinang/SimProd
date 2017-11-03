# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14553011.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 14553011
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) -> mu+ mu-) e+ nu_e]cc
#
from Configurables import Generation
Generation().EventType = 14553011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsienu,mm=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
