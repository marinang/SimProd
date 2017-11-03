# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14245001.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 14245001
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- ) p+ p~- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14245001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsipppi,mm=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
