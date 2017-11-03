# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14545012.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 14545012
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) (tau+ -> K+ pi+ pi- anti-nu_tau) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 14545012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,Kpipinu=DecProdCut,ffKiselev.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
