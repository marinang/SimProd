# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14143006.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14143006
#
# ASCII decay Descriptor: [B_c+ -> (psi(2S) -> mu+ mu- ) (a_1+ -> rho0 pi+ )]cc
#
from Configurables import Generation
Generation().EventType = 14143006
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_psi2Sa1,mmrhopi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
