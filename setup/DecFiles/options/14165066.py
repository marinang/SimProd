# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165066.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14165066
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> pi+ K- pi+) (K*0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14165066
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Kst0Ds,Kpi,piKpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
