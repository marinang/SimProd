# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165204.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14165204
#
# ASCII decay Descriptor: [B_c+ -> (D_s*+ -> (D_s+ -> K+ pi- pi+) gamma) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 14165204
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_PhiDsst,KK,Dsgamma,Kpipi=DecProdCut,BcVegPy,HELAMP010.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
