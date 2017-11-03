# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14177020.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14177020
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D+ -> K- pi+ pi+) (K*(892)0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14177020
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiD+Kst,mmKpipiKpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
