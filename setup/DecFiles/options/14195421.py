# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195421.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 14195421
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> K+ K- pi+ pi0) (anti-D0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14195421
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsD0,KKpipi0,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
