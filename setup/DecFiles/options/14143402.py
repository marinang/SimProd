# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14143402.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 14143402
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) (rho(770)+ -> pi+ (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 14143402
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsirho,mm=WeightedBcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
