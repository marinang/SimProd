# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14295002.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14295002
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ => K- K+ pi+) (D~0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14295002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsD0-DDalitz=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
