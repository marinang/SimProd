# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14299000.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 14299000
#
# ASCII decay Descriptor: [ B_c+ => (D*(2010)+ => (D0 => K- pi+ pi- pi+) pi+) (D~0 => K+ pi- pi+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 14299000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstD0,D0pi+,Kpipipi,Kpipipi=BcVegPy,DecProdCut,D0IncoherentSum.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
