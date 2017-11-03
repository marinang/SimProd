# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14573102.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14573102
#
# ASCII decay Descriptor: [B_c+ -> (D*0 -> (D0 -> K- pi+) gamma) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14573102
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Dst0munu=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
