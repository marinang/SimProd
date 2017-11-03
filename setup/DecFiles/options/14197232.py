# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14197232.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14197232
#
# ASCII decay Descriptor: [B_c+ => (D*_s+ => (D_s+ -> K- K+ pi+) gamma) (D*(2007)~0 => (D~0 -> K+ pi- pi+ pi-) gamma) ]CC
#
from Configurables import Generation
Generation().EventType = 14197232
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsstDst0,Dsgamma,KKpi,D0gamma,Kpipipi=BcVegPy,DecProdCut,HELAMP101.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
