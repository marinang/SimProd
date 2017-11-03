# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14877500.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14877500
#
# ASCII decay Descriptor: [B_c+ -> K+ (D*0 -> (D0 -> (K_S0 -> pi+ pi-) pi+ pi- pi0) pi0) (J/psi -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 14877500
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiD0,mm,D0+=cocktail,pipipi=DecProdCut,CntCut.dec"
Generation().Special.CutTool = "BcChargedNumInLHCb"
from Configurables import BcChargedNumInLHCb
Generation().Special.addTool( BcChargedNumInLHCb )
Generation().Special.BcChargedNumInLHCb.MuNumInLHCb = 2
Generation().Special.BcChargedNumInLHCb.HadNumInLHCb = 3
Generation().Special.BcChargedNumInLHCb.HadPt = 250.
Generation().Special.BcChargedNumInLHCb.MuPt = 450.
