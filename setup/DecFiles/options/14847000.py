# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14847000.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14847000
#
# ASCII decay Descriptor: [B_c+ -> (tau+ -> pi+ pi- pi+ anti-nu_tau) (psi(2S) -> (J/psi -> mu+ mu-) pi+ pi-) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14847000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_excitedtrueCharmoniumTauNu,charmonium+=cocktail,mm,pipipi=DecProdCut,CntCut.dec"
Generation().Special.CutTool = "BcChargedNumInLHCb"
from Configurables import BcChargedNumInLHCb
Generation().Special.addTool( BcChargedNumInLHCb )
Generation().Special.BcChargedNumInLHCb.MuNumInLHCb = 2
Generation().Special.BcChargedNumInLHCb.HadNumInLHCb = 3
Generation().Special.BcChargedNumInLHCb.HadPt = 250.
Generation().Special.BcChargedNumInLHCb.MuPt = 450.
