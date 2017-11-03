# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14545403.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14545403
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (tau+ -> pi+ pi+ pi- pi0 anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14545403
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,pipipipi0nu=DecProdCut,ffEbert.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.0
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 3.14
