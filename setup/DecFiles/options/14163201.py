# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14163201.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14163201
#
# ASCII decay Descriptor: [B_c+ -> (D_s1(2536)+ ->  (D*(2007)0 -> (D0 -> K- pi+) gamma) K+ )  gamma]cc
#
from Configurables import Generation
Generation().EventType = 14163201
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Ds1gamma,Dst0K,D0gamma,Kpi=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
