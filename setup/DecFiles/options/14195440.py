# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195440.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 14195440
#
# ASCII decay Descriptor: [ B_c+ => (D*(2010)+ => (D+ -> K- pi+ pi+) pi0) (D~0 -> K+ pi-) ]CC
#
from Configurables import Generation
Generation().EventType = 14195440
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstD0,D+pi0,Kpipi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
