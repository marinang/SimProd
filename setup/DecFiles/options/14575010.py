# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14575010.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 14575010
#
# ASCII decay Descriptor: [B_c+ -> ([B_s0]nos -> (D_s- => K+ K- pi-) pi+, [B_s0]os -> (D_s+ -> K+ K- pi+) pi-) anti-nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 14575010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bsmunu,Dspi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
