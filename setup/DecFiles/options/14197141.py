# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14197141.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 14197141
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> (K_S0 -> pi+ pi-) K+) (anti-D0 -> K+ pi- pi- pi+)]cc
#
from Configurables import Generation
Generation().EventType = 14197141
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsD0,KSK,Kpipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
