# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14145051.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14145051
#
# ASCII decay Descriptor: [B_c+ -> (B+ -> (J/psi -> mu+ mu-) K+ ) (rho0 -> pi- pi+) ]cc
#
from Configurables import Generation
Generation().EventType = 14145051
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BuRho,JpsiK,mumu=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
