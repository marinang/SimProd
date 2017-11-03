# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14495422.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14495422
#
# ASCII decay Descriptor: [( B_c+ => (D*_s+ => (D_s+ -> K- K+ pi+) (gamma||pi0) ) (D~0 -> K+ pi-) ) || ( B_c+ => (D_s+ -> K- K+ pi+) (D*(2007)~0 => (D~0 -> K+ pi-) (gamma||pi0) ) )]CC
#
from Configurables import Generation
Generation().EventType = 14495422
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsDst0,KKpi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
