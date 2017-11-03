# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14297463.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 14297463
#
# ASCII decay Descriptor: [ B_c+ => (D_s+ => K- K+ pi+) (D*(2007)~0 => (D~0 => K+ pi- pi+ pi-) pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14297463
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsDst0,KKpi,D0pi0,Kpipipi=BcVegPy,LooseNeutralCut,D0IncoherentSum.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
