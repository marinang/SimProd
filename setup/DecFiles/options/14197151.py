# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14197151.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 14197151
#
# ASCII decay Descriptor: [B_c+ -> ( D_s+ -> ( K*(892)+ -> (K_S0 -> pi+ pi- ) pi+ ) (anti-K*(892)0 -> K- pi+) ) (anti-D0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14197151
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsD0,KstKst0,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
