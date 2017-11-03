# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14375214.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14375214
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D_s*+ -> (D_s+ -> pi+ pi- pi+) gamma/pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14375214
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDsStar+,mmpipipi=DDalitz,DecProdCut,Az.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
