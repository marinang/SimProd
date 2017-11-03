# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165067.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 14165067
#
# ASCII decay Descriptor: [B_c+ -> (D_s+ -> pi+ pi- pi+) (K*0 -> K+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 14165067
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Kst0Ds,Kpi,pipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
