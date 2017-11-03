# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14133400.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 14133400
#
# ASCII decay Descriptor: [B_c+ -> (J/psi -> p+ anti-p-) (rho+ -> pi+ pi0)]cc
#
from Configurables import Generation
Generation().EventType = 14133400
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsirho,pp=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
