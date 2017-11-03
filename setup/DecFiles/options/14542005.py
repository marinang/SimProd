# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14542005.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14542005
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu-) (tau+ -> pi+ pi+ pi- pi0 nu_tau~) nu_tau]CC
#
from Configurables import Generation
Generation().EventType = 14542005
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,pipipipi0nu=DecProdCut,BcVegPy,taulababar.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
