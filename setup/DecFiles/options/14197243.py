# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14197243.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14197243
#
# ASCII decay Descriptor: [ B_c+ => (D_s+ -> K- K+ pi+) (D*(2007)~0 => (D~0 -> K+ pi- pi+ pi-) gamma) ]CC
#
from Configurables import Generation
Generation().EventType = 14197243
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsDst0,KKpi,D0gamma,Kpipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
