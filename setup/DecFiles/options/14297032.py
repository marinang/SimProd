# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14297032.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14297032
#
# ASCII decay Descriptor: [ B_c+ => (D*(2010)+ => (D0 => K- pi+ pi- pi+) pi+) (D~0 => K+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 14297032
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstD0,D0pi+,Kpipipi,Kpi=BcVegPy,DecProdCut,D0IncoherentSum.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
