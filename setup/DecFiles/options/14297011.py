# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14297011.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14297011
#
# ASCII decay Descriptor: [ B_c+ -> (B_s0 -> (D_s+ => K+ K- pi+) (D_s- => pi+ pi- pi-)) K+]cc
#
from Configurables import Generation
Generation().EventType = 14297011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_BsK+_DsDs,KKpi3pi=DDALTIZ,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
