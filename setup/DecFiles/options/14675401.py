# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14675401.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14675401
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (D_s+ -> (tau+ -> pi+ pi+ pi- pi0 anti-nu_tau) nu_tau)]cc
#
from Configurables import Generation
Generation().EventType = 14675401
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiInclc,TauNu,pipipipi0nu=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
