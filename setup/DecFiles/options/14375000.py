# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14375000.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 14375000
#
# ASCII decay Descriptor: {[B_c+ -> (D_s+ -> K+ K- pi+) e+ mu-]cc,[B_c+ -> (D_s+ -> K+ K- pi+) e- mu+]cc}
#
from Configurables import Generation
Generation().EventType = 14375000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dsemu,Kpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
