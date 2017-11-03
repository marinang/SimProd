# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14145031.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 14145031
#
# ASCII decay Descriptor: [B_c+ -> ([B+]nos -> (J/psi -> mu+ mu-) K+ ) K- pi+ ]cc
#
from Configurables import Generation
Generation().EventType = 14145031
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BuK-pi+_JpsiK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
