# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14145050.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 14145050
#
# ASCII decay Descriptor: [B_c+ -> (B+ -> (J/psi -> mu+ mu-) K+ ) pi+ pi- ]cc
#
from Configurables import Generation
Generation().EventType = 14145050
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bupipi,JpsiK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
