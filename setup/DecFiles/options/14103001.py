# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103001.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 14103001
#
# ASCII decay Descriptor: [B_c+ -> (rho(770)0 -> pi+ pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_rho0pi+=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
