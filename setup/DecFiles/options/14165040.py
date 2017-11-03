# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165040.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 14165040
#
# ASCII decay Descriptor: [B_c+ -> (B+ -> (anti-D0 -> K+ pi-) pi+ ) pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 14165040
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bupipi,D0pi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
