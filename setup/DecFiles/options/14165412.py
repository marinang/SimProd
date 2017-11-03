# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165412.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14165412
#
# ASCII decay Descriptor: [B_c+ -> (D*+ -> (D+ -> pi+ K- pi+) pi0) (K*0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14165412
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Kst0Dst,Kpi,Dpi0,piKpi=DDalitz,BcVegPy,DecProdCut,HELAMP100.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
