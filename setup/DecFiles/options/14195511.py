# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195511.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 14195511
#
# ASCII decay Descriptor: [B_c+ -> (D+ -> (K_S0 -> pi+ pi- ) pi+ pi0) (anti-D0 -> K+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 14195511
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+D0,KSpipi0,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
