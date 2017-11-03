# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14177001.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14177001
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (D*(2010)+ -> (D0 -> K- pi+) pi+) (K*(892)0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14177001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDst+Kst,mmD0pi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
