# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14133040.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 14133040
#
# ASCII decay Descriptor: [B_c+ -> (chi_c2 -> pi+ pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14133040
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_chic2pi,pipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
