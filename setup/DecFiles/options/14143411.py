# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14143411.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14143411
#
# ASCII decay Descriptor: [B_c+ -> (Jpsi -> mu+ mu-) (K*+ -> (pi0 -> gamma gamma) K+ )]cc
#
from Configurables import Generation
Generation().EventType = 14143411
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiKst,mm,pi0K,gg=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
