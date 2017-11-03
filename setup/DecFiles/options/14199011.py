# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14199011.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14199011
#
# ASCII decay Descriptor: [B_c+ -> (D*+ -> (D0 -> K- pi+ pi+ pi-) pi+) (anti-D0 -> K+ pi- pi- pi+)]cc
#
from Configurables import Generation
Generation().EventType = 14199011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstD0,Kpipipi,Kpipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
