# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14497421.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 14497421
#
# ASCII decay Descriptor: [( B_c+ => (D*(2010)+ => (D+ -> K- pi+ pi+) (gamma||pi0) ) (D~0 -> K+ pi- pi+ pi-) ) || ( B_c+ => (D+ -> K- pi+ pi+) (D*(2007)~0 => (D~0 -> K+ pi- pi+ pi-) (gamma||pi0) ) )]CC
#
from Configurables import Generation
Generation().EventType = 14497421
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+Dst0,Kpipi,Kpipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
