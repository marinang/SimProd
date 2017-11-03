# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14643048.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 14643048
#
# ASCII decay Descriptor: [B_c+ => (J/psi(1S) => mu+ mu-) (tau+ => mu+ nu_mu nu_tau~) nu_tau]CC
#
from Configurables import Generation
Generation().EventType = 14643048
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiTauNu,mununu=BcVegPy,ffEbert.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
