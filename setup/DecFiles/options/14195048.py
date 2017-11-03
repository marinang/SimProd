# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195048.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 14195048
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> K+ K- pi+) (anti-D0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14195048
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D0Ds,Kpi,KKpi=DDalitz,BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
