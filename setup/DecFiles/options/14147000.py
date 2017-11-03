# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14147000.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 14147000
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- ) pi+ pi+ pi- pi- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14147000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsipipipipipi,mm=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
