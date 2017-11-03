# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14875600.py generated: Fri, 03 Nov 2017 08:48:37
#
# Event Type: 14875600
#
# ASCII decay Descriptor: [B_c+ -> (D_s*+ -> (D_s+ -> (eta' -> (rho0 -> pi+ pi-) gamma) (rho+ -> pi+ pi0)) gamma) (J/psi -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 14875600
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiDs,mm,Ds+=cocktail,pipipi=DecProdCut,CntCut.dec"
Generation().Special.CutTool = "BcChargedNumInLHCb"
from Configurables import BcChargedNumInLHCb
Generation().Special.addTool( BcChargedNumInLHCb )
Generation().Special.BcChargedNumInLHCb.MuNumInLHCb = 2
Generation().Special.BcChargedNumInLHCb.HadNumInLHCb = 3
Generation().Special.BcChargedNumInLHCb.HadPt = 250.
Generation().Special.BcChargedNumInLHCb.MuPt = 450.
