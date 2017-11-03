# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195461.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 14195461
#
# ASCII decay Descriptor: [ B_c+ => (D+ => K- pi+ pi+) (D*(2007)~0 => (D~0 => K+ pi-) pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14195461
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+Dst0,Kpipi,D0pi0,Kpi=BcVegPy,LooseNeutralCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
